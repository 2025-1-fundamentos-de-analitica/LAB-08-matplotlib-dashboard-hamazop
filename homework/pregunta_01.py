# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

import matplotlib.pyplot as plt
import pandas as pd
import os

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    os.makedirs("docs", exist_ok=True)
    
    df = pd.read_csv("files/input/shipping-data.csv")
    df_ware = df.copy()
    plt.figure()
    counts = df_ware["Warehouse_block"].value_counts()
    counts.plot.bar(
        title="Shipping per Warehouse",
        xlabel="Warehouse block",
        ylabel="Record count",
        color="tab:blue",
        fontsize=8
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("docs/shipping_per_warehouse.png")
    
    df_mode=df.copy()
    plt.figure()
    counts = df_mode["Mode_of_Shipment"].value_counts()
    counts.plot.pie(
        title="Mode of shipment",
        wedgeprops=dict(width=0.35),
        ylabel="",
        colors=["tab:blue", "tab:orange", "tab:green"],
    )
    plt.savefig("docs/mode_of_shipment.png")
    
    df_rating=df.copy()
    plt.figure()
    df_rating = (df_rating[["Mode_of_Shipment", "Customer_rating"]].groupby("Mode_of_Shipment").describe())
    df_rating.columns = df_rating.columns.droplevel()
    df_rating = df_rating[["mean", "min", "max"]] 
    plt.barh(
        y = df_rating.index.values,
        width=df_rating["max"].values - 1,
        left=df_rating["min"].values,
        height=0.9,
        color = "lightgray",
        alpha = 0.8,
    )   
    
    colors = [
        "tab:green" if value >= 3.0 else "tab:orange" for value in df_rating["mean"].values
    ]
    
    plt.barh(
        y = df_rating.index.values,
        width=df_rating["mean"].values - 1,
        left=df_rating["min"].values,
        height=0.5,
        color=colors,
        alpha=1.0,
    )
    plt.title("Average Customer Rating")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["bottom"].set_visible(False)
    plt.savefig("docs/average_customer_rating.png")
    
    df_weight=df.copy()
    plt.figure()
    df_weight.Weight_in_gms.plot.hist(
        title="Shipping weight distribution",
        color="tab:orange",
        edgecolor="white",
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("docs/weight_distribution.png")

    return 0