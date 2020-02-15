# Backend

To instantiate the project you have to clone it and download the [Drugbank full database](https://drive.google.com/open?id=19pHYY-BsFJkoMKp2MPKl3QKzv5bHx_t3) at the root of the project.

You should also setup Neo4J and copy the `.env.example` file as `.env` with your credentials.

You can run the #1, #2, #6 cells in `drugbankparser.ipynb` to extract some data from the Drugban database and export them in CSV. Then you can run `neo4jsample.py` to persist those data in your triplestore.
