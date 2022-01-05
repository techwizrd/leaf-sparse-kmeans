import random
import warnings
import time
import numpy as np
import compressors
from sklearn.preprocessing import MinMaxScaler


class Client:
    
    def __init__(self, client_id, group=None, train_data={'x' : [],'y' : []}, eval_data={'x' : [],'y' : []}, model=None):
        self._model = model
        self.id = client_id
        self.group = group
        self.train_data = train_data
        self.eval_data = eval_data

    def train(self, num_epochs=1, batch_size=10, minibatch=None):
        """Trains on self.model using the client's train_data.

        Args:
            num_epochs: Number of epochs to train. Unsupported if minibatch is provided (minibatch has only 1 epoch)
            batch_size: Size of training batches.
            minibatch: fraction of client's data to apply minibatch sgd,
                None to use FedAvg
        Return:
            comp: number of FLOPs executed in training process
            num_samples: number of samples used in training
            update: set of weights
            update_size: number of bytes in update
        """

        # TODO: Swap this for a with statement and a timer
        train_start = time.time()

        if minibatch is None:
            data = self.train_data
            comp, update = self.model.train(data, num_epochs, batch_size)
        else:
            frac = min(1.0, minibatch)
            num_data = max(1, int(frac*len(self.train_data["x"])))
            xs, ys = zip(*random.sample(list(zip(self.train_data["x"], self.train_data["y"])), num_data))
            data = {'x': xs, 'y': ys}

            # Minibatch trains for only 1 epoch - multiple local epochs don't make sense!
            num_epochs = 1
            comp, update = self.model.train(data, num_epochs, num_data)
        num_train_samples = len(data['y'])

        train_stop = time.time()
        train_time = int(round(train_stop - train_start))

        before_nonzeros = 0
        after_nonzeros = 0

        ### Start Compression
        compress_start = time.time()

        layers_to_compress = [6]
        update = np.array(update, dtype=object)
        for i in layers_to_compress:
            actual_shape = update[i].shape
            flattended = update[i].flatten()
            before_nonzeros += np.count_nonzero(flattended)
            compressed_flat = flattended

            # For calculating sparsity constraints
            flat_sz = flattended.size
            bits = flattended.size * flattended.itemsize * 8
            B_j = int(np.floor(0.60 * bits))
            scaler = MinMaxScaler()
            Xsc  = flattended.reshape((flat_sz, 1))
            Xsc = scaler.fit_transform(Xsc)

            try:
                Cg, _ = compressors.sparse_kmeans(
                        gradient=Xsc,
                        budget=B_j
                        )
                compressed_flat = scaler.inverse_transform(Cg.reshape((flat_sz, 1)))
                compressed_flat = compressed_flat.flatten()
            except BaseException as err:
                print("ERROR")
                print(f"Unexpected err={err}, type(err)={type(err)}")
                print(flattended)
                exit

            after_nonzeros += np.count_nonzero(compressed_flat)
            update[i] = compressed_flat.reshape(actual_shape)

        compress_end = time.time()
        ### End Compression

        compress_time = int(round(compress_end - compress_start))
        train_time_secs = train_time + compress_time

        return comp, num_train_samples, before_nonzeros, after_nonzeros, update, train_time_secs

    def test(self, set_to_use='test'):
        """Tests self.model on self.test_data.
        
        Args:
            set_to_use. Set to test on. Should be in ['train', 'test'].
        Return:
            dict of metrics returned by the model.
        """
        assert set_to_use in ['train', 'test', 'val']
        if set_to_use == 'train':
            data = self.train_data
        elif set_to_use == 'test' or set_to_use == 'val':
            data = self.eval_data
        return self.model.test(data)

    @property
    def num_test_samples(self):
        """Number of test samples for this client.

        Return:
            int: Number of test samples for this client
        """
        if self.eval_data is None:
            return 0
        return len(self.eval_data['y'])

    @property
    def num_train_samples(self):
        """Number of train samples for this client.

        Return:
            int: Number of train samples for this client
        """
        if self.train_data is None:
            return 0
        return len(self.train_data['y'])

    @property
    def num_samples(self):
        """Number samples for this client.

        Return:
            int: Number of samples for this client
        """
        train_size = 0
        if self.train_data is not None:
            train_size = len(self.train_data['y'])

        test_size = 0 
        if self.eval_data is not  None:
            test_size = len(self.eval_data['y'])
        return train_size + test_size

    @property
    def model(self):
        """Returns this client reference to model being trained"""
        return self._model

    @model.setter
    def model(self, model):
        warnings.warn('The current implementation shares the model among all clients.'
                      'Setting it on one client will effectively modify all clients.')
        self._model = model
