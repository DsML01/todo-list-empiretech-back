from http import HTTPStatus


def test_create_task_success(client):
    """Testa a criação de uma tarefa com dados válidos."""

    priority = 3

    payload = {
        'title': 'Testar Backend',
        'description': 'Garantir que os testes passam',
        'priority': priority,
    }
    response = client.post('/api/tasks/', json=payload)
    data = response.get_json()

    assert response.status_code == HTTPStatus.CREATED
    assert data['title'] == 'Testar Backend'
    assert data['priority'] == priority
    assert 'id' in data


def test_create_task_invalid_data(client):
    """Testa erro de validação (Pydantic) ao enviar título vazio."""
    payload = {'title': '', 'priority': 1}
    response = client.post('/api/tasks/', json=payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_get_tasks(client):
    """Testa a listagem de tarefas."""
    # Criamos uma tarefa primeiro
    client.post('/api/tasks/', json={'title': 'Levar o cachorro para passear'})

    response = client.get('/api/tasks/')
    data = response.get_json()

    assert response.status_code == HTTPStatus.OK
    assert len(data) == 1
    assert data[0]['title'] == 'Levar o cachorro para passear'


def test_update_task_partial(client):
    """Testa o PATCH (atualização parcial)."""
    # Cria
    res_create = client.post(
        '/api/tasks/',
        json={'title': 'Esse é o título original'}
    )
    task_id = res_create.get_json()['id']

    # Atualiza apenas o status
    response = client.patch(
        f'/api/tasks/{task_id}', json={'is_completed': True}
    )
    data = response.get_json()

    assert response.status_code == HTTPStatus.OK
    assert data['is_completed'] is True
    assert data['title'] == 'Esse é o título original'


def test_delete_task(client):
    """Testa a remoção de uma tarefa."""
    res_create = client.post(
        '/api/tasks/',
        json={'title': 'Essa é a tarefa a ser deletada'}
    )
    task_id = res_create.get_json()['id']

    response = client.delete(f'/api/tasks/{task_id}')
    assert response.status_code == HTTPStatus.NO_CONTENT

    # Verifica se sumiu
    res_get = client.get('/api/tasks/')
    assert len(res_get.get_json()) == 0
