# Сергеева Анна - 11 когорта, Финальный проект. Инженер по тестированию плюс

import sender_stand_request


# Проверка 200 кода
def test_get_track():
    data_order = sender_stand_request.get_order(sender_stand_request.track_number)
    assert data_order.status_code == 200


    print("Номер заказа", sender_stand_request.track_number)