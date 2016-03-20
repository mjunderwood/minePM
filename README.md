# minePM


Download MongoDB via:

https://www.mongodb.org/downloads?_ga=1.258611594.1275616774.1458435026#production

Install python mongo framework (pymongo)
  - sudo pip install pymongo

Database Setup:
  - Type "mongod" into your shell to create a running mongo instance
  - Type mongo to access the command line interface for the db
  - To create a db you type "use minepm", Database named minepm created.
  - For the script you will need three collections (repos for json data)
      - db.createCollection("bladdercancer")
      - db.createCollection("lungcancer")
      - db.createCollection("prostatecancer")
  - To see whats in a collection you type "db.<collectionname>.find().pretty()"
  - run the script --> "python biofetch.py"
  - Depending on the parameter set in the main function for updateData(), valid options are "bladder","lung","prostate", it will pull in ~10k articles into the proper collection.
  
