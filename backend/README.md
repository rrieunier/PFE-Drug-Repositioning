# Backend

## Make it up and running
### Dependencies
```bash
conda install flask
pip install neo4j python-dotenv
```
### Data
To instantiate the project you have to download the [Drugbank full database](https://drive.google.com/open?id=19pHYY-BsFJkoMKp2MPKl3QKzv5bHx_t3) at the root of the project.

You shall also setup Neo4J and duplicate the `.env.example` file as `.env` with your Neo4J credentials.

You can run the #1, #2, #6 cells in `drugbankparser.ipynb` to extract some data from the Drugbank database and export them in CSV. Then you can run `neo4jsample.py` to persist those data in your triplestore.

### Backend
If you want to run the backend along the frontend, then you have to run those commands:
```bash
cd backend
chmod +x server.sh
./server.sh
```
It will run the server in DEBUG mode so that any change in the code restarts the server. To disable the DEBUG mode, replace the first line of `server.sh` with `export FLASK_DEBUG=0`. **Please be patient, it is long to load the database in memory, it takes approximately less than one minute to complete and run the server**.
