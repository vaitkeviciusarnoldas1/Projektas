from data_manager import DatabaseManager
from prettytable import PrettyTable
import os
from dotenv import load_dotenv

load_dotenv()

def print_table(results):
    """Spausdina lentelę naudojant PrettyTable"""
    if not results:
        print("No data found.")
        return

    table = PrettyTable()
    table.field_names = results[0].keys()  # Automatiškai nustato stulpelių pavadinimus
    for row in results:
        table.add_row(row.values())
    print(table)

def drop_table(manager, table_name):
    """Pašalina lentelę, jei ji egzistuoja"""
    drop_table_query = f"DROP TABLE IF EXISTS {table_name};"
    manager.execute_query(drop_table_query)
    print(f"Table '{table_name}' dropped successfully (if existed).")

def create_table(manager, table_name, table_schema):
    """Sukuria lentelę"""
    create_table_query = f"CREATE TABLE {table_name} ({table_schema});"
    manager.execute_query(create_table_query)
    print(f"Table '{table_name}' created successfully.")

def insert_data(manager, table_name, insert_query):
    """Įterpia duomenis į lentelę"""
    manager.execute_query(insert_query)
    print(f"Data inserted successfully into '{table_name}' table.")

def update_data(manager, table_name, update_query):
    """Atnaujina duomenis lentelėje"""
    manager.execute_query(update_query)
    print(f"Data updated successfully in '{table_name}' table.")

def delete_data(manager, table_name, delete_query):
    """Ištrina duomenis iš lentelės"""
    manager.execute_query(delete_query)
    print(f"Data deleted successfully from '{table_name}' table.")

def select_data(manager, table_name):
    """Rodo lentelės turinį"""
    query = f"SELECT * FROM {table_name};"
    print(f"Executing query: {query}")
    results = manager.fetch_all(query)
    if results:
        keys = [desc[0] for desc in manager.get_cursor_description()]
        results_dict = [dict(zip(keys, row)) for row in results]
        print_table(results_dict)
    else:
        print("No data found.")

def list_tables_and_contents(manager):
    """Išspausdina visų lentelių turinį iš informacijos schemos"""
    query = """
    SELECT table_name 
    FROM information_schema.tables
    WHERE table_schema = 'public';
    """
    tables = manager.fetch_all(query)
    if not tables:
        print("No tables found in the database.")
        return

    for table in tables:
        table_name = table[0]
        print(f"Contents of the '{table_name}' table:")
        select_data(manager, table_name)
        print()  # Tuščia eilutė tarp lentelių

def main():
    db_name = os.getenv("DATABASE_NAME")
    db_user = os.getenv("DB_USERNAME")
    db_password = os.getenv("PASSWORD")
    db_host = os.getenv("HOST")
    db_port = os.getenv("DB_PORT")

    manager = DatabaseManager(db_name, db_user, db_password, db_host, db_port)

    try:
        manager.connect()
        print("Database connected")

        list_tables_and_contents(manager)
        table_name = "Treneris"
        table_schema = """
        treneris_id SERIAL PRIMARY KEY,
        vardas VARCHAR(50) NOT NULL,
        pavarde VARCHAR(50) NOT NULL,
        amzius INT NOT NULL,
        el_pastas VARCHAR(100),
        telefonas VARCHAR(20),
        licencijos_nr VARCHAR(20),
        licencijos_galiojimo_laikas DATE,
        patirtis VARCHAR(50),
        sporto_sritis VARCHAR(50)
        """
        insert_query = f"""
        INSERT INTO {table_name} (vardas, pavarde, amzius, el_pastas, telefonas, licencijos_nr, licencijos_galiojimo_laikas, patirtis, sporto_sritis)
        VALUES
        ('Arnoldas', 'Vaitkevicius', 35, 'arnoldas@gmail.com', '+370111111111', 'L1234', '2025-01-01', '5 metai', 'Salės treneris'),
        ('Darius', 'Vaitkevicius', 40, 'darius@gmail.com', '+37062222222', 'L1235', '2025-01-02', '10 metai', 'Kardio treneris'),
        ('Justas', 'Vaitkevicius', 45, 'jutas@gmail.com', '+37063333333', 'L1236', '2025-01-03', '15 metai', 'Fitneso treneris'),
        ('Nojus', 'Vaitkevicius', 30, 'nojus@gmail.com', '+37064444444', 'L1237', '2025-01-04', '3 metai', 'Jogos treneris'),
        ('Kristina', 'Vaitkevice', 28, 'kristina@gmail.com', '+370655555555', 'L1238', '2025-01-05', '2 metai', 'Plaukimo treneris');
        """
        update_query = f"""
        UPDATE {table_name}
        SET el_pastas = 'arnoldas1@gmail.com'
        WHERE vardas = 'Arnoldas';
        """
        delete_query = f"DELETE FROM {table_name} WHERE amzius < 30;"

        # Pašalinti lentelę, jei ji egzistuoja
        drop_table(manager, table_name)

        # Sukurti lentelę
        create_table(manager, table_name, table_schema)

        # Įterpti duomenis
        insert_data(manager, table_name, insert_query)

        # Rodyti lentelės turinį prieš pakeitimus
        print(f"Contents of the '{table_name}' table before updates:")
        select_data(manager, table_name)

        # Atnaujinti duomenis
        update_data(manager, table_name, update_query)

        # Ištrinti duomenis
        delete_data(manager, table_name, delete_query)

        # Rodyti lentelės turinį po pakeitimų
        print(f"Contents of the '{table_name}' table after updates:")
        select_data(manager, table_name)

        # Pašalinti lentelę
        drop_table(manager, table_name)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        manager.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()
