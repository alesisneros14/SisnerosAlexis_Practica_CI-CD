from app import app

def test_hello_world():
    """
    Test que verifica la página de inicio.
    Comprueba que la respuesta sea 200 OK y que contenga el saludo al profesor.
    """
    # Creamos un cliente de prueba para la aplicación
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hola, profe!" in response.data