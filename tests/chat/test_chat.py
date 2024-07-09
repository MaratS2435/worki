# import requests
# import pytest
#
# BASE_URL = "http://localhost:1323"  # Замените на ваш реальный базовый URL
#
#
# def test_create_chat():
#     url = f"{BASE_URL}/chats"
#     data = {
#         "users_id": "New Chat",  # Убедитесь, что это соответствует структуре models.ChatToCreate
#         "messages_id": "This is a new chat"
#     }
#
#     response = requests.post(url, json=data)
#
#     assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
#
#     chat = response.json()
#
#     assert 'id' in chat, "Chat ID should be in the response"
#     assert chat['name'] == "New Chat"
#     assert chat['description'] == "This is a new chat"
#     assert 'created_at' in chat, "Creation timestamp should be in the response"
#     print(f"Chat created successfully with ID {chat['id']}")
