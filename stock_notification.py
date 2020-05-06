{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "import twstock\n",
    "import requests\n",
    "twstock.__update_codes()\n",
    "\n",
    "def get_price(stock_id):\n",
    "    info=twstock.realtime.get(stock_id)\n",
    "    if info['success']:\n",
    "        return (info['info']['name'],info['realtime']['latest_trade_price'])\n",
    "    else:\n",
    "        return (False,False)\n",
    "\n",
    "def get_best(stock_id):\n",
    "    stock=twstock.Stock(stock_id)\n",
    "    bp=twstock.BestFourPoint(stock).best_four_point()\n",
    "    if bp:\n",
    "        return ('買進' if bp[0] else '賣出', bp[1])\n",
    "    else:\n",
    "        return (False,False)\n",
    "    \n",
    "def get_setting():\n",
    "    txt=input('text file name:')\n",
    "    txt=txt +'.txt'\n",
    "    res=[]\n",
    "    try:\n",
    "        with open(txt) as f:\n",
    "            dlist=f.readlines()\n",
    "            print('讀入:',dlist)\n",
    "            for lst in dlist:\n",
    "                s=lst.split(',')\n",
    "                res.append(s[0].strip,float(s[1]),float(s[2]))\n",
    "    except:\n",
    "        print(txt +'讀取錯誤')\n",
    "    \n",
    "    return res\n",
    "\n",
    "def send_ifttt(v1,v2,v3):\n",
    "    url=('https://maker.ifttt.com/trigger/toLINE/with/key/' +\n",
    "         'mxYRhKKS3u9DvCAqR5rrrWr3glzMyg3QtWRpTQbi4nG' +\n",
    "        '?value1=' + str(v1) +\n",
    "        '&value2=' +str(v2) + \n",
    "        '&value3=' + str(v3))\n",
    "    r=requests.get(url)\n",
    "    if r.text[:5]=='Congr':\n",
    "        print('已傳送(' + str(v1) + ', ' + str(v2) +', ' + str(v3) + ' )到LINE')\n",
    "    else:\n",
    "        print('errrror')\n",
    "    return r.text\n",
    "\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
