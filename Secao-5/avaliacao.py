from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd
import numpy as np



boston_dataset = load_boston()
boston_dataset

dados = pd.DataFrame(data= boston_dataset.data, columns= boston_dataset.feature_names)
dados = dados.drop(['INDUS', 'CHAS'], axis= 1)

log_precos = np.log(boston_dataset.target)
objetivo = pd.DataFrame(data= log_precos, columns= ['PRICE'])



CRIME_IDX = 0
ZN_IDX = 1
CHAS_IDX = 2
RM_IDX = 4
PTRATIO_IDX = 8
ZILLOW_MEDIAN_PRICE = 583.3
FATOR = ZILLOW_MEDIAN_PRICE / np.median(boston_dataset.target)




casa_stat = np.ndarray(shape= (1, 11))
casa_stat = dados.mean().values.reshape(1,11)




regr = LinearRegression().fit(dados, objetivo)
previsto = regr.predict(dados)

MSE = mean_squared_error(objetivo, previsto, squared= True)
RMSE = mean_squared_error(objetivo, previsto, squared= False)




def obter_estimativa_log(n_quartos,
                    estudantes_por_turma,
                    proximo_rio= False,
                   alta_fidelidade= True):
    #Configurando
    
    casa_stat[0][RM_IDX] = n_quartos
    casa_stat[0][PTRATIO_IDX] = estudantes_por_turma
    casa_stat[0][CHAS_IDX] = proximo_rio
    
    
    # Prevendo
    
    estimativa_log = regr.predict(casa_stat)[0][0]
    if(alta_fidelidade):
        margem_acima = estimativa_log + 2*RMSE
        margem_abaixo = estimativa_log - 2*RMSE
        intervalo = 95
    else:
        margem_acima = estimativa_log + RMSE
        margem_abaixo = estimativa_log - RMSE
        intervalo = 68
    
    
    return estimativa_log, margem_acima, margem_abaixo, intervalo






def obter_estimativa_em_dolar(rm, ptratio,
                          chas=False,
                          large_range= True):
    
    """  Retorna o valor da estimativa de preço em dolares, de uma casa em Boston a partir
        dos parametros
        
        Parametros:
        ---------------
        
        rm: Numero de quartos na residencia
        ptratio: Numero de estudantes por professor na area
        chas: True se a casa for perto do rio, falso se não
        large_range: True para uma precisão de 95%, False para 68%
    
    """
    
    
    if rm < 1 or ptratio < 1:
        print("Valor inválido, tente novamente")
        return
    
    est_log, maximo, minimo, intervalo = obter_estimativa_log(n_quartos=  rm,
                    estudantes_por_turma= ptratio,
                    proximo_rio= True,
                   alta_fidelidade= False)
    
    est_dolar = np.e**est_log * 1000
    est_maxima = np.e**maximo * 1000
    est_minima = np.e**minimo * 1000
    
    
    est_aprox = np.around(est_dolar, -3)
    est_aprox_min = np.around(est_maxima, -3)
    est_aprox_max = np.around(est_minima, -3)
    
    
    
    return est_aprox, est_aprox_min, est_aprox_max, intervalo