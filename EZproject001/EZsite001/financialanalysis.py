import datetime
import os

import numpy as np
import quandl
import matplotlib.pyplot as plt
from dateutil import tz
from pandas.plotting import register_matplotlib_converters
from mpl_toolkits.mplot3d import Axes3D

register_matplotlib_converters()


def getorigintime():
    tz_sh = tz.gettz('Asia/Shanghai')
    now = datetime.datetime.now(tz=tz_sh)
    return now


def gettime():
    return getorigintime().strftime('%Y-%m-%d')


def getdata():
    golddata = quandl.get("SHFE/AUZ2020", authtoken="EDHKCFxMS-fA8rLYvvef", start_date="2019-11-18",
                          end_date=gettime())
    return golddata


def getcurrentdata():
    golddata = getdata()
    currentdate = gettime()
    try:
        currentdata = golddata.loc[str(currentdate), ['Open', 'Close', 'High', 'Low', 'Settle']].values
    except Exception:
        currentdate = (getorigintime() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        currentdata = golddata.loc[str(currentdate), ['Open', 'Close', 'High', 'Low', 'Settle']].values
    finally:
        return currentdata.tolist()


def plot_price_trend(time, name):
    golddata = getdata()
    currenttime_ymd = str(gettime())
    data = golddata.loc[str(time):currenttime_ymd, ['Open', 'Close', 'High', 'Low', 'Settle']]
    x = data.index
    y_open = data['Open'].values
    y_close = data['Close'].values
    y_high = data['High'].values
    y_low = data['Low'].values
    y_settle = data['Settle'].values
    plt.title(name, color='gold', fontsize='large', fontweight='bold')
    plt.figure(dpi=300)
    # border of axis x and y
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('gold')
    ax.spines['left'].set_color('gold')
    ax.spines['right'].set_color('none')
    plt.plot(x, y_open, label="Open Price")
    plt.plot(x, y_close, label="Close Price")
    plt.plot(x, y_high, label="High Price", ls='--')
    plt.plot(x, y_low, label="Low Price", ls='--')
    plt.plot(x, y_settle, label="Settle Price", marker='.')
    # change axis value for longer than 1 month
    if name == '2months' or name == '3months':
        x_display = []
        for index, value in enumerate(x):
            if index % 7 == 0:
                x_display.append(value.strftime('%m-%d'))
            else:
                x_display.append('')
    else:
        x_display = []
        for index, value in enumerate(x):
            x_display.append(value.strftime('%m-%d'))
    # axis x and y
    plt.xticks(x, x_display, color='gold', rotation='45')
    plt.yticks(color='gold')
    plt.legend()
    pwd = os.path.dirname(os.path.dirname(__file__))
    saveplace = pwd + '/static/pfas/img/' + name + '.png'
    plt.savefig(saveplace, transparent=True)


def plot_price_table(time, name):
    golddata = getdata()
    currenttime_ymd = str(gettime())
    data = golddata.loc[str(time):currenttime_ymd, ['Open', 'Close', 'High', 'Low', 'Settle']]
    plt.figure()
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    plt.xticks([])
    plt.yticks([])
    col_labels = data.index.strftime('%m-%d')
    row_labels = ['Open', 'Close', 'Settle', 'High', 'Close']
    table_vals = data.values.tolist()
    plt.table(cellText=table_vals, rowLabels=row_labels, colLabels=col_labels, loc='center')
    pwd = os.path.dirname(os.path.dirname(__file__))
    saveplace = pwd + '/static/pfas/img/' + name + '.png'
    plt.savefig(saveplace, transparent=True)


def plot_3D(name):
    golddata = getdata()
    data = golddata.loc[:, ['Settle']]
    data2 = golddata.loc[:, ['Volume']]
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    y = data.values.tolist()
    y_new = [float(v) for i in y for v in i]
    y = y_new
    z = data2.values.tolist()
    z_new = [float(v) for i in z for v in i]
    z = z_new
    x = [i for i in range(len(y))]
    ax.plot(x, y, zs=0, zdir='z', label='curve in (x,y)', color='gold')
    ax.scatter(xs=x, zs=z, ys=y, zdir='z', label='points in (x,y,z)', c='gold')
    ax.legend()
    ax.title.set_color('gold')
    ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.set_xlabel('Days')
    ax.set_ylabel('Settle Price')
    ax.set_zlabel('Volume')
    ax.view_init(elev=35, azim=-45)
    plt.xticks(color='gold')
    plt.yticks(color='gold')
    ax.tick_params(axis='z', colors='gold')
    ax.xaxis.label.set_color('gold')
    ax.yaxis.label.set_color('gold')
    ax.zaxis.label.set_color('gold')

    pwd = os.path.dirname(os.path.dirname(__file__))
    saveplace = pwd + '/static/pfas/img/' + name + '.png'
    plt.savefig(saveplace, transparent=True)
    # plt.show()


def gethistorydata():
    currenttime = getorigintime()
    # 1 week table
    aweek_table = (currenttime - datetime.timedelta(days=6)).strftime('%Y-%m-%d')
    plot_price_table(aweek_table, gettime())
    # 1 week trend
    aweek = (currenttime - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    plot_price_trend(aweek, '1week')
    # 2 weeks
    twoweeks = (currenttime - datetime.timedelta(days=14)).strftime('%Y-%m-%d')
    plot_price_trend(twoweeks, '2weeks')
    # 3 weeks
    threeweeks = (currenttime - datetime.timedelta(days=21)).strftime('%Y-%m-%d')
    plot_price_trend(threeweeks, '3weeks')
    # 1 month
    onemonth = (currenttime - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
    plot_price_trend(onemonth, '1month')
    # 2 months
    twomonths = (currenttime - datetime.timedelta(days=60)).strftime('%Y-%m-%d')
    plot_price_trend(twomonths, '2months')
    # 3 months
    threemonths = (currenttime - datetime.timedelta(days=90)).strftime('%Y-%m-%d')
    plot_price_trend(threemonths, '3months')
    # All data 3D
    plot_3D('allin')
    return "success"


if __name__ == '__main__':
    # pass
    print(gethistorydata())

