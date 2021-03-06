import numpy as np
from sklearn.metrics import accuracy_score, f1_score
from sklearn.neighbors import KNeighborsClassifier

import config as CONFIG
from classifier.util import data_util


def run_cv(n_neighbors=50, data_source='', activities=None, permutate_xyz=False):
    kfold_data = data_util.load_kfolds_training_and_testing_data(
        scaler_name=CONFIG.MODEL_NAMES['minmax_scaler'],
        k=5,
        source=data_source,
        activities=activities,
        permutate_xyz=permutate_xyz
    )

    accuracy_results = []
    fscore_results = []

    print('Data Source: {}'.format(data_source))
    print('Number of Neighbors: {}'.format(n_neighbors))
    print('Sampling Frequency: {}'.format(CONFIG.SAMPLING_FREQUENCY))
    print('Window Size: {}'.format(CONFIG.WINDOW_SIZE))
    print('Training Source: {}'.format(CONFIG.KFOLD_DATA_SOURCE_SUBJECT))
    print('Activities: {}'.format(activities))
    print('Permutate XYZ: {}'.format(permutate_xyz))
    print()

    for i, data in enumerate(kfold_data):
        X_train = data[0]
        X_test = data[1]
        Y_train = data[2]
        Y_test = data[3]

        model = KNeighborsClassifier(n_neighbors=n_neighbors, n_jobs=-1)
        model.fit(X_train, Y_train)
        predictions = model.predict(X_test)

        accuracy = accuracy_score(Y_test, predictions)
        accuracy_results.append(accuracy)

        fscore = f1_score(Y_test, predictions, average='weighted')
        fscore_results.append(fscore)

    accuracy_mean = np.mean(accuracy_results)
    accuracy_std_dev = np.std(accuracy_results)

    fscore_mean = np.mean(fscore_results)
    fscore_std_dev = np.std(fscore_results)


    print('Accuracy: {}'.format(accuracy_results))
    print('Accuracy Mean: {}, Accuracy Standard deviation: {}'.format(accuracy_mean, accuracy_std_dev))
    print('F1 Score: {}'.format(fscore_results))
    print('F1 Mean: {}, F1 Standard deviation: {}'.format(fscore_mean, fscore_std_dev))
    print()
    print()
    print()

    return accuracy_mean, accuracy_std_dev, fscore_mean, fscore_std_dev


if __name__ == '__main__':
    n_neighbors = [1, 3, 5, 7, 10, 15, 20]

    for n in n_neighbors:
        accuracy_mean, accuracy_std_dev, fscore_mean, fscore_std_dev = run_cv(
            n_neighbors=n,
            data_source='',
            permutate_xyz=False,
            activities=[
                'brushing',
                'folding',
                'going_downstairs',
                'going_upstairs',
                'lying',
                'reading',
                'running',
                'sitting',
                'standing',
                'sweeping_the_floor',
                'food_preparation',
                'typing',
                'walking',
                'writing'
            ]
        )