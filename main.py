import numpy as np

from CubicSplineCustom import CubicSplineCustom
from Universo import Universo
from NewtonCustom import simular_projetil_com_newton

VELOCIDADE_PROJETIL = 5e4


if __name__ == "__main__":
    universo = Universo()
    solucao = universo.simular()

    terra = next(c for c in universo.corpos_celestes if c.name == "Terra")
    terra_x0, terra_y0 = terra.trace[0]

    asteroide = next(c for c in universo.corpos_celestes if c.name == "Asteroide")
    trajetoria_x = [p[0] for p in asteroide.trace]
    trajetoria_y = [p[1] for p in asteroide.trace]
    lista_tempos = np.linspace(0, universo.duracao, len(trajetoria_x))

    spline_real_x = CubicSplineCustom(lista_tempos, trajetoria_x)
    spline_real_y = CubicSplineCustom(lista_tempos, trajetoria_y)

    df_trajetoria_projetil = None

    params = {
        "posicao_x_asteroide": trajetoria_x,
        "posicao_y_asteroide": trajetoria_y,
        "tempos_asteroide": lista_tempos,
        "velocidade_projetil": VELOCIDADE_PROJETIL,
        "po_x": terra_x0,
        "po_y": terra_y0,
        "spline_x": spline_real_x,
        "spline_y": spline_real_y,
    }

    df_trajetoria_projetil = simular_projetil_com_newton(**params)
    

    universo.animar(solucao, df_trajetoria_projetil=df_trajetoria_projetil)