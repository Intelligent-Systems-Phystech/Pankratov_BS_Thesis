import numpy as np
import pickle
from scipy import sparse

from pyartm import regularizers
from pyartm.optimizations import balanced
from pyartm.common import experiments
from pyartm.optimizations import default
from collection import generate
from collection import modify
from analysis import metrics_definition
from analysis import metrics_count

ITERS_COUNT = 1 #Оптимальное число здесь ~ 300, число итераций работы алгоритма
SAMPLES = 1

def perform_experiment(
   train_n_dw_matrix, test_n_dw_matrix, optimizer,
   T, samples, output_path , tau , path_phi_output 
):
   "Проводит эксперимент. Сохраняет его результаты в output_path и полученную матрицу phi в path_phi_output."
    optimizer.iteration_callback = experiments.default_callback(
        train_n_dw_matrix = train_n_dw_matrix,
        test_n_dw_matrix = test_n_dw_matrix,
        top_pmi_sizes = [5, 10, 20, 30],
        top_avg_jaccard_sizes = [10, 50, 100, 200],
        measure_time = False
    )

    for seed in range(samples):
        expphi, exptheta = experiments.default_sample(train_n_dw_matrix, T, seed, optimizer, tau  )
    optimizer.iteration_callback.save_results(output_path)
    with open(path_phi_output, 'wb') as resource_file:
        pickle.dump(expphi, resource_file) 
    return (expphi, exptheta)

def basic_experiment(data_list, tau_list, num_topics):
    "tau_list должен содержать None для сравнения с default"
    "data_list - адреса сохраненных матриц n_dw"
    regularization_list = [regularizers.Trivial()] * ITERS_COUNT
    for data_addr in data_list:
        with open(data_addr, 'rb') as f:
            data = pickle.load(f)
        data = sparse.csr_matrix(np.array(data)) # исходная генерация генерирует именно list
        for t in tau_list:
            perform_experiment(
                data, None, default.Optimizer(regularization_list), 100, 
                SAMPLES, output_path = 'exp_{}_{}.pkl'.format(t, data_addr), tau = t, 
                path_phi_output = 'expphi_{}_{}.pkl'.format(t, data_addr)
            )

def full_experiment():
    "Все числовые параметры можно менять, параметры здесь выбраны из разумности полученных результатов"
    phi = generate.generate_phi(0.01,100,10000)
    theta = generate.generate_theta(0.1,2000,100)
    data_list = []
    for one_topic_docs in (5, 10, 12, 15):  #число документов во всех темах,кроме одной
        Dt_array = [one_topic_docs for i in range (100)]
        Dt_array[0] = 2000 - (99 * one_topic_docs)
        theta_modified = modify.modify_theta(theta, Dt_array, 2000)
        test_collection = generate.generate_collection(2000, phi, theta, num_words_in_doc = 2000)
        with open('collection_{}'.format(one_topic_docs), 'wb') as data_file:
            pickle.dump(test_collection, data_file)
        data_list.append('collection_{}'.format(one_topic_docs))
        with open('phi_{}'.format(one_topic_docs), 'wb') as phi_file:
            pickle.dump(phi, phi_file)
        with open('theta_{}'.format(one_topic_docs), 'wb') as theta_file:
            pickle.dump(theta, theta_file)
    basic_experiment(data_list, [None], 100)
    for one_topic_docs in (5, 10, 12, 15): 
        with open('phi_{}'.format(one_topic_docs), 'rb') as phi_file:
            phi = pickle.load(phi_file)
        with open('expphi_{}_collection_{}.pkl'.format(None,one_topic_docs), 'rb') as phi_file:
            phi_exp = pickle.load(phi_file)
        print(one_topic_docs)
        metrics_count.check_metrics(phi, phi_exp.transpose(), 100)
        
