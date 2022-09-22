{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "733b32df",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "import scrape\n",
    "\n",
    "\n",
    "app = Flask(__name__)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "id": "6f357f87",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__' (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# Use flask_pymongo to set up mongo connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)\n",
    "mars_db = mongo.db.mars\n",
    "\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    scraped_data = mars_db.find_one()\n",
    "    #print(scraped_data[\"hemisphere_images\"])\n",
    "    return render_template(\"index.html\", mars = scraped_data)\n",
    "\n",
    "@app.route(\"/scrape\")\n",
    "\n",
    "\n",
    "def scrape_all():\n",
    "    mars_dict = scrape.scrape_all()\n",
    "    ##mars_dict.insert_one(mars_data)\n",
    "    scraped_data.update_one({}, {\"$set\": mars_data}, upsert=True)\n",
    "    return redirect(\"/\", code = 302)\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "id": "4e1dcb68",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
