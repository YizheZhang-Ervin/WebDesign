import datetime
import os
import quandl
import matplotlib.pyplot as plt
from dateutil import tz
from pandas.plotting import register_matplotlib_converters


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
        currentdata = golddata.loc[str(currentdate), ['Open', 'Close', 'High', 'Low']].values
    except Exception:
        currentdate = (getorigintime() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        currentdata = golddata.loc[str(currentdate), ['Open', 'Close', 'High', 'Low']].values
    finally:
        return currentdata.tolist()


def plot_price(time, name):
    golddata = getdata()
    currenttime_ymd = str(gettime())
    data = golddata.loc[str(time):currenttime_ymd, ['Open', 'Close', 'High', 'Low']]
    x = data.index
    y_open = data['Open'].values
    y_close = data['Close'].values
    y_high = data['High'].values
    y_low = data['Low'].values
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
    # number of axis x and y
    plt.xticks(x, color='gold', rotation='60')
    plt.yticks(color='gold')
    plt.legend()
    pwd = os.path.dirname(os.path.dirname(__file__))
    saveplace = pwd+'/static/pfas/img/'+name+'.png'
    plt.savefig(saveplace, transparent=True)


def gethistorydata():
    currenttime = getorigintime()
    # 1 day
    aweek = (currenttime - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    plot_price(aweek, gettime())
    # 1 week
    aweek = (currenttime - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    plot_price(aweek, '1week')
    # 2 weeks
    twoweeks = (currenttime - datetime.timedelta(days=14)).strftime('%Y-%m-%d')
    plot_price(twoweeks, '2weeks')
    # 3 weeks
    threeweeks = (currenttime - datetime.timedelta(days=21)).strftime('%Y-%m-%d')
    plot_price(threeweeks, '3weeks')
    # 1 month
    onemonth = (currenttime - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
    plot_price(onemonth, '1month')
    # 2 months
    twomonths = (currenttime - datetime.timedelta(days=60)).strftime('%Y-%m-%d')
    plot_price(twomonths, '2months')
    # 3 months
    threemonths = (currenttime - datetime.timedelta(days=90)).strftime('%Y-%m-%d')
    plot_price(threemonths, '3months')
    return "success"


if __name__ == '__main__':
    # pass
    print(getorigintime())
