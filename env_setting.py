import os
import time


class Setting(object):
    def __init__(self, log=None):
        self.V = {

            'GODS_PERSPECTIVE': True,
            # Map Info
            'MAP_X': 16,
            'MAP_Y': 16,

            # Observation
            'NUM_UAV': 2,
            'INIT_POSITION': [(8., 8.), (8., 8.)],
            'OBSER_X': 80,
            'OBSER_Y': 80,
            'OBSER_C': 3,

            # Action
            'ACT_NUM': 3,

            # max moving distance within one time step
            'MAXDISTANCE': 1.,
            'MIN_DISTANCE': 1e-4,

            # value in obeservation [80.80.3]
            'BORDER_VALUE': -1.,
            'POWER_VALUE': -1.,  # power station value in observation 2
            'BORDER_WIDTH': 4,
            # initial energy of a uav
            'ENERGY': 40.,  # TODO new  40.
            'DELTA_ENERGY': 10.,
            'MINI_ENEGY': 20.,
            'DISTANCE_ENERGY_FACTOR': 0.1,
            'POI_ENERGY_FACTOR': 1.,
            # end


            'MAX_VALUE': 1.,
            'MIN_VALUE': 0.,

            # c speed
            'COLLECTION_PROPORTION': 0.2,
            # data collecting range
            'RANGE': 1.1,
            'VISIT': 1. / 1000.,

            # Penalty and reward
            'OBSTACLE_PENALTY': -1.,
            'LESS_ENEGY_PENALTY': -1.,
            'DATA_REWARD': 1.,
            'WASTE_STEP': -.5,
            'NORMALIZE': 0.1,
            # Penalty and reward
            # 'BETA': 0.01,
            'EPSILON': 1e-4,

            # 'POWER_NUM': 5,
            # 'POWER':[[4,12],[8,8],[14,10],[2,4],[10,2]],
            # 'POWER_NUM': 5,
            # 'POWER':[[4,12],[8,8],[12,10],[2,4],[10,2]],
            # #
            # 'POWER_NUM': 2,
            # 'POWER': [[4, 12],[12,10]],
            #
            'POWER_NUM': 1,
            'POWER': [[4, 12]],

            'MINI_ENERGY_RATIO': 0.,
            'REWARD_POW_RATIO': 1.2,
            'PoI': [[7.33642578e-02, 2.69531250e-01, 2.81494141e-01],
                    [8.95019531e-01, 9.73632812e-01, 2.92480469e-01],
                    [5.00000000e-01, 2.69775391e-01, 5.78613281e-01],
                    [2.56591797e-01, 9.40917969e-01, 1.86279297e-01],
                    [5.30273438e-01, 4.57031250e-01, 3.90380859e-01],
                    [3.30322266e-01, 3.19580078e-01, 2.03979492e-01],
                    [1.23413086e-01, 6.88476562e-02, 7.76367188e-01],
                    [1.02767944e-02, 9.99023438e-01, 8.34472656e-01],
                    [6.66015625e-01, 6.83593750e-01, 2.68310547e-01],
                    [8.75488281e-01, 5.19042969e-01, 9.21386719e-01],
                    [6.89941406e-01, 1.40991211e-01, 2.58300781e-01],
                    [4.75585938e-01, 9.25781250e-01, 6.91894531e-01],
                    [6.16455078e-02, 2.71911621e-02, 3.36914062e-01],
                    [6.19506836e-02, 8.25683594e-01, 3.84033203e-01],
                    [6.01562500e-01, 1.92749023e-01, 5.58593750e-01],
                    [6.74804688e-01, 7.32910156e-01, 3.62060547e-01],
                    [5.38574219e-01, 6.76757812e-01, 1.43356323e-02],
                    [8.76953125e-01, 7.98339844e-01, 4.41650391e-01],
                    [8.70605469e-01, 2.06176758e-01, 4.76074219e-01],
                    [5.47363281e-01, 2.02026367e-01, 6.69921875e-01],
                    [8.03222656e-01, 2.40234375e-01, 5.81542969e-01],
                    [9.87792969e-01, 1.49917603e-02, 9.50336456e-02],
                    [4.52148438e-01, 1.66625977e-01, 9.69238281e-01],
                    [1.27441406e-01, 7.05337524e-03, 1.44531250e-01],
                    [3.00537109e-01, 8.23730469e-01, 8.95996094e-01],
                    [3.09326172e-01, 9.25292969e-01, 8.89160156e-01],
                    [4.48486328e-01, 4.97802734e-01, 2.10937500e-01],
                    [3.92089844e-01, 5.18188477e-02, 3.69140625e-01],
                    [7.15942383e-02, 7.82714844e-01, 3.21044922e-01],
                    [8.25683594e-01, 6.38671875e-01, 3.76220703e-01],
                    [8.36914062e-01, 7.09472656e-01, 2.81250000e-01],
                    [9.45312500e-01, 8.15917969e-01, 7.89550781e-01],
                    [2.42065430e-01, 5.84472656e-01, 9.02832031e-01],
                    [9.34082031e-01, 1.72241211e-01, 3.70849609e-01],
                    [3.54736328e-01, 4.90234375e-01, 9.87304688e-01],
                    [3.50585938e-01, 1.26586914e-01, 3.50585938e-01],
                    [3.67675781e-01, 4.57763672e-01, 2.13378906e-01],
                    [3.50097656e-01, 5.02441406e-01, 3.24951172e-01],
                    [9.12597656e-01, 8.50219727e-02, 2.12280273e-01],
                    [8.03222656e-01, 5.37597656e-01, 1.59423828e-01],
                    [9.46289062e-01, 6.02050781e-01, 2.34985352e-01],
                    [3.37646484e-01, 9.49096680e-03, 9.97070312e-01],
                    [3.85498047e-01, 5.94726562e-01, 1.81427002e-02],
                    [9.70214844e-01, 7.64648438e-01, 4.93652344e-01],
                    [6.06933594e-01, 1.90673828e-01, 5.24902344e-02],
                    [7.98339844e-02, 4.51660156e-01, 6.46484375e-01],
                    [6.64550781e-01, 4.71679688e-01, 8.91113281e-01],
                    [1.95770264e-02, 8.50585938e-01, 8.79394531e-01],
                    [6.83593750e-01, 3.07006836e-02, 9.87304688e-01],
                    [9.70703125e-01, 7.96508789e-02, 6.67480469e-01],
                    [7.52929688e-01, 1.40380859e-01, 2.69775391e-01],
                    [5.69824219e-01, 8.32031250e-01, 8.64257812e-01],
                    [6.37817383e-02, 1.97143555e-01, 2.38769531e-01],
                    [7.71484375e-01, 2.25708008e-01, 8.58764648e-02],
                    [7.44628906e-01, 5.01953125e-01, 4.51904297e-01],
                    [9.37988281e-01, 6.22558594e-01, 8.70117188e-01],
                    [5.26855469e-01, 6.06933594e-01, 4.72656250e-01],
                    [8.54980469e-01, 8.50585938e-01, 8.12500000e-01],
                    [6.50878906e-01, 6.57714844e-01, 2.10449219e-01],
                    [8.08593750e-01, 7.40722656e-01, 2.78808594e-01],
                    [9.27734375e-02, 5.13183594e-01, 5.23925781e-01],
                    [3.51806641e-01, 9.97070312e-01, 5.85327148e-02],
                    [4.28955078e-01, 8.54003906e-01, 5.02929688e-01],
                    [6.23046875e-01, 6.21582031e-01, 5.11718750e-01],
                    [1.46362305e-01, 3.22265625e-02, 2.14721680e-01],
                    [2.77587891e-01, 5.43945312e-01, 4.75097656e-01],
                    [6.47460938e-01, 6.01074219e-01, 2.17651367e-01],
                    [7.26074219e-01, 3.05175781e-01, 2.01904297e-01],
                    [9.89257812e-01, 3.91113281e-01, 5.16967773e-02],
                    [1.44531250e-01, 3.56201172e-01, 6.53320312e-01],
                    [3.28613281e-01, 2.26898193e-02, 5.79589844e-01],
                    [1.28295898e-01, 2.81982422e-01, 5.55664062e-01],
                    [7.54394531e-01, 3.95751953e-01, 1.58203125e-01],
                    [5.08499146e-03, 9.56420898e-02, 1.45751953e-01],
                    [2.80517578e-01, 2.45483398e-01, 9.68261719e-01],
                    [6.14257812e-01, 5.58105469e-01, 9.96093750e-01],
                    [8.23242188e-01, 9.62890625e-01, 5.07812500e-01],
                    [3.18603516e-01, 5.28808594e-01, 6.60156250e-01],
                    [7.75390625e-01, 4.06494141e-01, 9.83886719e-01],
                    [8.04199219e-01, 2.16674805e-01, 6.63085938e-01],
                    [6.67114258e-02, 5.15441895e-02, 7.69531250e-01],
                    [4.19433594e-01, 3.65478516e-01, 6.98730469e-01],
                    [4.94140625e-01, 8.50219727e-02, 6.94824219e-01],
                    [6.36230469e-01, 1.24145508e-01, 5.36132812e-01],
                    [6.64062500e-01, 4.07958984e-01, 6.56250000e-01],
                    [7.74902344e-01, 8.01269531e-01, 7.56835938e-01],
                    [3.46679688e-01, 5.14648438e-01, 1.89575195e-01],
                    [2.05322266e-01, 3.16894531e-01, 3.40576172e-01],
                    [5.24902344e-01, 6.85501099e-03, 2.66601562e-01],
                    [2.33276367e-01, 7.70996094e-01, 9.94140625e-01],
                    [5.28808594e-01, 3.14208984e-01, 8.60839844e-01],
                    [1.37084961e-01, 9.77050781e-01, 6.05957031e-01],
                    [7.54882812e-01, 9.38964844e-01, 9.48242188e-01],
                    [5.38085938e-01, 3.28674316e-02, 6.04003906e-01],
                    [8.00292969e-01, 9.02832031e-01, 4.09912109e-01],
                    [6.88964844e-01, 1.45996094e-01, 5.25390625e-01],
                    [9.54589844e-01, 4.43359375e-01, 3.99780273e-02],
                    [7.43408203e-02, 7.23632812e-01, 9.20410156e-01],
                    [7.80273438e-01, 6.44042969e-01, 1.51596069e-02],
                    [5.42480469e-01, 8.46557617e-02, 4.81262207e-02],
                    [2.50732422e-01, 5.39550781e-01, 6.81152344e-01],
                    [1.36230469e-01, 4.08630371e-02, 7.01660156e-01],
                    [6.25488281e-01, 9.60449219e-01, 4.90722656e-02],
                    [3.14208984e-01, 5.43945312e-01, 4.24072266e-01],
                    [2.53173828e-01, 9.02832031e-01, 4.40917969e-01],
                    [1.02783203e-01, 4.94628906e-01, 1.53198242e-01],
                    [2.78076172e-01, 2.03735352e-01, 2.65625000e-01],
                    [8.38867188e-01, 5.37597656e-01, 3.07617188e-02],
                    [4.91638184e-02, 5.19531250e-01, 6.07910156e-01],
                    [4.47509766e-01, 1.69372559e-03, 4.80712891e-01],
                    [5.84472656e-01, 3.07861328e-01, 8.44238281e-01],
                    [9.79492188e-01, 8.03222656e-01, 7.20703125e-01],
                    [1.40014648e-01, 5.45898438e-01, 7.52929688e-01],
                    [8.14941406e-01, 1.98608398e-01, 6.80175781e-01],
                    [7.00195312e-01, 7.81250000e-03, 2.94189453e-01],
                    [7.82226562e-01, 6.59179688e-01, 9.01855469e-01],
                    [5.02929688e-01, 5.54687500e-01, 9.96582031e-01],
                    [3.27636719e-01, 5.03417969e-01, 2.96142578e-01],
                    [7.20214844e-01, 2.51220703e-01, 8.77441406e-01],
                    [9.37988281e-01, 3.42529297e-01, 2.68554688e-01],
                    [9.46777344e-01, 8.13476562e-01, 4.30664062e-01],
                    [1.79565430e-01, 7.67135620e-03, 8.56933594e-01],
                    [6.37695312e-01, 9.58496094e-01, 9.68750000e-01],
                    [4.66552734e-01, 2.22778320e-01, 5.78613281e-01],
                    [9.94628906e-01, 3.46679688e-01, 3.96728516e-01],
                    [7.42187500e-01, 6.86523438e-01, 4.22851562e-01],
                    [4.24072266e-01, 3.41552734e-01, 6.34277344e-01],
                    [7.58300781e-01, 4.00146484e-01, 9.92675781e-01],
                    [1.00463867e-01, 7.52441406e-01, 8.96972656e-01],
                    [2.21435547e-01, 4.53948975e-03, 7.00683594e-01],
                    [1.59179688e-01, 3.56933594e-01, 3.71093750e-01],
                    [9.75585938e-01, 7.82226562e-01, 1.44287109e-01],
                    [1.97021484e-01, 2.02178955e-02, 2.55859375e-01],
                    [2.22473145e-02, 4.82177734e-01, 7.26074219e-01],
                    [8.56445312e-01, 3.43505859e-01, 4.72167969e-01],
                    [9.41894531e-01, 4.56054688e-01, 1.66503906e-01],
                    [2.03247070e-01, 8.99414062e-01, 9.60937500e-01],
                    [7.68066406e-01, 6.76757812e-01, 5.68359375e-01],
                    [5.50781250e-01, 4.30175781e-01, 4.83398438e-01],
                    [8.86230469e-01, 4.58007812e-01, 1.02050781e-01],
                    [7.96875000e-01, 2.96142578e-01, 7.21191406e-01],
                    [2.00683594e-01, 7.11914062e-01, 2.91748047e-01],
                    [4.01611328e-01, 5.70800781e-01, 8.74023438e-01],
                    [9.42382812e-01, 9.16992188e-01, 6.76757812e-01],
                    [4.33593750e-01, 1.40258789e-01, 8.36914062e-01],
                    [3.09814453e-01, 2.40966797e-01, 5.59082031e-01],
                    [5.71289062e-01, 8.16894531e-01, 8.78417969e-01],
                    [5.39550781e-01, 4.43847656e-01, 9.95117188e-01],
                    [2.49145508e-01, 8.94042969e-01, 8.72070312e-01],
                    [5.73730469e-01, 4.72412109e-01, 6.66992188e-01],
                    [6.44531250e-01, 6.50390625e-01, 9.58984375e-01],
                    [4.36035156e-01, 9.52148438e-01, 8.22265625e-01],
                    [1.97265625e-01, 4.88525391e-01, 1.81152344e-01],
                    [6.44531250e-01, 9.41406250e-01, 2.84912109e-01],
                    [9.19433594e-01, 4.14306641e-01, 1.68457031e-01],
                    [8.89160156e-01, 8.33496094e-01, 8.52050781e-01],
                    [5.00488281e-01, 2.39013672e-01, 1.78588867e-01],
                    [9.31152344e-01, 7.51953125e-01, 6.45019531e-01],
                    [9.85839844e-01, 8.89648438e-01, 7.42675781e-01],
                    [7.87109375e-01, 6.16699219e-01, 2.25952148e-01],
                    [9.09179688e-01, 1.62597656e-01, 7.76855469e-01],
                    [9.66796875e-01, 2.04833984e-01, 9.41772461e-02],
                    [3.28613281e-01, 7.63183594e-01, 1.40380859e-01],
                    [6.14746094e-01, 8.26660156e-01, 3.44238281e-01],
                    [1.36962891e-01, 5.34179688e-01, 2.84271240e-02],
                    [3.02978516e-01, 9.28710938e-01, 3.76464844e-01],
                    [6.22070312e-01, 8.33007812e-01, 8.69628906e-01],
                    [7.18261719e-01, 2.03369141e-01, 9.60449219e-01],
                    [2.69775391e-01, 6.86035156e-01, 7.48046875e-01],
                    [4.23095703e-01, 8.95996094e-01, 5.03921509e-03],
                    [8.61328125e-01, 3.87939453e-01, 4.07714844e-01],
                    [1.15234375e-01, 8.13964844e-01, 5.51269531e-01],
                    [5.08300781e-01, 3.02490234e-01, 3.99169922e-01],
                    [5.12695312e-02, 5.16601562e-01, 7.35351562e-01],
                    [7.18261719e-01, 9.92187500e-01, 9.40429688e-01],
                    [9.06738281e-01, 9.29687500e-01, 3.18603516e-01],
                    [7.37792969e-01, 7.26074219e-01, 8.36425781e-01],
                    [1.18103027e-02, 4.26330566e-02, 6.30859375e-01],
                    [7.88085938e-01, 5.09277344e-01, 1.24755859e-01],
                    [5.54687500e-01, 2.45239258e-01, 9.16748047e-02],
                    [9.44335938e-01, 4.91943359e-01, 3.21777344e-01],
                    [9.37988281e-01, 4.94628906e-01, 1.44775391e-01],
                    [4.56787109e-01, 8.32519531e-01, 2.20092773e-01],
                    [3.61816406e-01, 7.36816406e-01, 5.19042969e-01],
                    [7.36328125e-01, 7.96386719e-01, 7.63671875e-01],
                    [2.84271240e-02, 8.34960938e-01, 2.22656250e-01],
                    [1.61254883e-01, 2.37915039e-01, 7.39257812e-01],
                    [7.20214844e-01, 6.17187500e-01, 7.19238281e-01],
                    [6.13769531e-01, 8.34472656e-01, 3.78906250e-01],
                    [7.03613281e-01, 3.82995605e-03, 1.10839844e-01],
                    [1.11572266e-01, 8.80859375e-01, 9.24804688e-01],
                    [2.37792969e-01, 5.97656250e-01, 7.20703125e-01],
                    [5.69335938e-01, 3.29833984e-01, 2.56591797e-01],
                    [6.97265625e-01, 5.82031250e-01, 5.42480469e-01],
                    [9.76074219e-01, 8.06152344e-01, 3.95019531e-01],
                    [2.91015625e-01, 6.47949219e-01, 7.50488281e-01],
                    [2.36328125e-01, 1.01562500e-01, 6.90429688e-01],
                    [3.54614258e-02, 3.41796875e-01, 1.89331055e-01],
                    [4.40917969e-01, 8.55468750e-01, 6.16210938e-01],
                    [9.13085938e-01, 1.22619629e-01, 3.65905762e-02],
                    [1.09436035e-01, 8.11035156e-01, 6.42700195e-02],
                    [5.84960938e-01, 6.36718750e-01, 5.49316406e-01],
                    [1.78588867e-01, 3.01269531e-01, 4.47021484e-01],
                    [1.80541992e-01, 8.08593750e-01, 5.20996094e-01],
                    [6.27929688e-01, 4.38476562e-01, 4.32617188e-01],
                    [9.81445312e-01, 5.37109375e-01, 7.40234375e-01],
                    [2.02270508e-01, 8.41308594e-01, 6.25976562e-01],
                    [8.53027344e-01, 6.74316406e-01, 9.16137695e-02],
                    [5.69335938e-01, 9.65820312e-01, 2.50976562e-01],
                    [2.87109375e-01, 5.35156250e-01, 7.79785156e-01],
                    [3.71093750e-01, 6.81640625e-01, 9.40429688e-01],
                    [9.13574219e-01, 7.00683594e-01, 1.02905273e-01],
                    [5.00000000e-01, 5.58593750e-01, 6.46484375e-01],
                    [6.87500000e-01, 1.38671875e-01, 7.20214844e-01],
                    [2.05535889e-02, 1.13403320e-01, 8.75488281e-01],
                    [2.29003906e-01, 9.48730469e-01, 6.71386719e-01],
                    [2.24243164e-01, 6.50878906e-01, 3.56933594e-01],
                    [1.61499023e-01, 5.75561523e-02, 5.55175781e-01],
                    [1.93725586e-01, 9.69726562e-01, 4.04785156e-01],
                    [8.55468750e-01, 3.57666016e-02, 4.82666016e-01],
                    [1.29089355e-02, 7.27050781e-01, 6.25976562e-01],
                    [5.21972656e-01, 7.37792969e-01, 5.96191406e-01],
                    [4.75341797e-01, 2.03735352e-01, 2.97851562e-01],
                    [8.20800781e-01, 1.22802734e-01, 1.60644531e-01],
                    [2.80761719e-01, 1.07543945e-01, 5.24902344e-01],
                    [2.34130859e-01, 6.90429688e-01, 4.27734375e-01],
                    [9.66796875e-01, 1.17111206e-02, 7.00195312e-01],
                    [8.13964844e-01, 3.52539062e-01, 8.86230469e-01],
                    [2.95654297e-01, 6.84204102e-02, 5.57617188e-01],
                    [3.02490234e-01, 6.45996094e-01, 4.21630859e-01],
                    [6.57226562e-01, 9.38476562e-01, 1.52832031e-01],
                    [7.59765625e-01, 8.78417969e-01, 7.83691406e-01],
                    [6.04980469e-01, 6.04980469e-01, 3.24951172e-01],
                    [5.87890625e-01, 2.76367188e-01, 2.40722656e-01],
                    [5.23437500e-01, 9.62890625e-01, 2.18994141e-01],
                    [9.40551758e-02, 7.78808594e-01, 4.52880859e-01],
                    [9.13574219e-01, 5.56640625e-01, 8.66210938e-01],
                    [3.29589844e-01, 2.63519287e-02, 5.52246094e-01],
                    [4.27246094e-01, 1.13586426e-01, 5.00488281e-01],
                    [9.97558594e-01, 1.75781250e-02, 1.34887695e-01],
                    [7.00683594e-01, 1.01074219e-01, 2.36572266e-01],
                    [5.35156250e-01, 8.13476562e-01, 1.81762695e-01],
                    [3.52294922e-01, 2.31445312e-01, 4.08935547e-01],
                    [7.76855469e-01, 5.40527344e-01, 4.71191406e-01],
                    [2.14355469e-01, 8.48632812e-01, 6.66992188e-01],
                    [7.00195312e-01, 1.85424805e-01, 1.27807617e-01],
                    [1.04187012e-01, 8.95996094e-01, 8.00292969e-01],
                    [5.69152832e-02, 8.06640625e-01, 1.57348633e-01],
                    [1.58935547e-01, 5.29296875e-01, 8.51562500e-01],
                    [2.71728516e-01, 6.44531250e-01, 4.10888672e-01],
                    [7.23144531e-01, 9.79980469e-01, 1.96289062e-01],
                    [9.05761719e-01, 7.03125000e-01, 1.17340088e-02],
                    [3.24951172e-01, 3.52783203e-01, 9.37500000e-01],
                    [1.04980469e-01, 4.91943359e-01, 9.11132812e-01],
                    [5.57327271e-03, 2.04467773e-01, 4.24316406e-01],
                    [9.47265625e-01, 9.57519531e-01, 3.58886719e-01]],  # PoI in map [x,y,value]
            # 'OBSTACLE': [
            #     [0, 4, 1, 1],
            #     [0, 9, 1, 1],
            #     [2, 2, 2, 1],
            #     [3, 6, 4, 1],
            #     [4, 4, 1, 4],
            #     # [4,12, 1, 1],
            #     [5, 13, 1, 1],
            #     [6, 12, 2, 1],
            #     # [10,3, 1, 1],
            #     [10, 5, 3, 1],
            #     # [10,9, 1, 1],
            #     [11, 5, 1, 3],
            #     [10, 13, 1, 2],
            #     [11, 13, 2, 1],
            #     # [11,12,1, 2],
            #     [12, 0, 1, 2],
            #     [12, 5, 1, 1],
            #     [12, 7, 1, 1],
            #     # [12,13,2, 1],
            #     [15, 11, 1, 1]
            # ],  # obstacle in map [x,y,w,h]
            'OBSTACLE': [
                [0, 4, 1, 1],
                [0, 9, 1, 1],
                [0, 10, 2, 1],
                [2, 2, 2, 1],
                [4, 6, 3, 1],
                [4, 5, 1, 3],
                # [4,12, 1, 1],
                [5, 13, 1, 1],
                [6, 12, 2, 1],
                [6, 7, 1, 1],
                [6, 5, 1, 1],
                # [10,3, 1, 1],
                [10, 5, 3, 1],
                # [10,9, 1, 1],
                [11, 5, 1, 3],
                [10, 13, 1, 2],
                [10, 7, 1, 1],
                [11, 13, 2, 1],
                # [11,12,1, 2],
                [12, 0, 1, 2],
                [12, 5, 1, 1],
                [12, 7, 1, 1],
                # [12,13,2, 1],
                [15, 11, 1, 1]
            ],  # obstacle in map [x,y,w,h]
            # 'OBSTACLE': [
            #     [0, 4, 1, 1],
            #     # [0, 9, 1, 1],
            #     [0, 10, 1, 1],
            #     [0, 15, 1, 1],
            #     [2, 2, 2, 1],
            #     [3, 6, 4, 1],
            #     [4, 2, 1, 1],
            #     [4, 3, 1, 1],
            #     [4, 4, 1, 3],
            #     # [4,12, 1, 1],
            #     [5, 13, 1, 1],
            #     [6, 12, 2, 1],
            #     # [10,3, 1, 1],
            #     # [10, 5, 2, 1],
            #     [10, 6, 2, 1],
            #     [10, 7, 2, 1],
            #     # [10,9, 1, 1],
            #     # [11, 5, 1, 2],
            #     [10, 13, 1, 1],
            #     [11, 13, 2, 1],
            #     # [11,12,1, 2],
            #     [12, 0, 1, 1],
            #     [12, 5, 1, 1],
            #     [12, 7, 1, 1],
            #     # [12,13,2, 1],
            #     [15, 11, 1, 1],
            #     [15, 0, 1, 1],
            # ],  # obstacle in map [x,y,w,h]
            # 'OBSTACLE': [
            #     # [4,0, 1, 1],
            #     [9, 0, 1, 1],
            #     [10, 0, 2, 1],
            #     [15, 0, 1, 1],
            #     # [2, 2, 2, 1],
            #     [6, 3, 4, 1],
            #     # [4, 2, 1, 1],
            #     [3, 5, 1, 1],
            #     [4, 4, 1, 3],
            #     # [4,12, 1, 1],
            #     [13, 5, 1, 1],
            #     [12, 6, 2, 1],
            #     # [10,3, 1, 1],
            #     [5, 10, 3, 1],
            #     [6, 10, 3, 1],
            #     [7, 10, 3, 1],
            #     # [10,9, 1, 1],
            #     [5,11, 1, 2],
            #     [13, 10, 1, 1],
            #     [13, 11, 2, 1],
            #     # [11,12,1, 2],
            #     [0, 12, 1, 1],
            #     [5, 12, 1, 1],
            #     # [7, 12, 1, 1],
            #     # [12,13,2, 1],
            #     [11, 15, 1, 1],
            #     [0, 15, 1, 1],
            # ],  # obstacle in map [x,y,w,h]
        }
        if log is not None:
            self.LOG = log
            self.time = log.time

    def log(self):
        # with open(os.path.join('.', self.time + '.txt'), 'x') as file:
        #     for key, value in self.V.items():
        #         print(key, value, file=file)
        self.LOG.log(self.V)
if __name__ == '__main__':
    import json

    settings = Setting()
    json_str = json.dumps(settings.V)
    print(json_str)
    print(type(json_str))

    new_dict = json.loads(json_str)

    print(new_dict)
    print(type(new_dict))


    with open("record.json", "w") as f:

        json.dump(new_dict, f)

        print("加载入文件完成...")