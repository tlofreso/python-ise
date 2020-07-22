def test_create_endpoint(test_devices, test_connection):
    mac = test_devices[0][0]
    group = test_devices[0][1]
    desc = test_devices[0][2]
    my_test = test_connection.create_endpoint(
        mac=mac, group_name=group, description=desc
    )

    assert my_test["status_code"] == 201


def test_update_endpoint(test_devices, test_connection):
    mac = test_devices[0][0]
    group = test_devices[0][1]
    desc = test_devices[0][2]
    my_test = test_connection.update_endpoint(
        mac=mac, group_name=group, description=desc, endpoint_name="AdamsPhone"
    )

    assert my_test["status_code"] == 200


def test_get_endpoint_by_mac(test_devices, test_connection):
    my_test = test_connection.get_endpoint_by_mac(test_devices[0][0])

    assert (
        my_test["status_code"] == 200 and my_test["json"]["SearchResult"]["total"] == 1
    )


def test_get_endpoint_by_name(test_devices, test_connection):
    my_test = test_connection.get_endpoint_by_name(test_devices[0][0])

    assert my_test["status_code"] == 200 and my_test["json"]["ERSEndPoint"] is not None


def test_delete_endpoint(test_devices, test_connection):
    mac = test_devices[0][0]
    my_test = test_connection.delete_endpoint(mac=mac)

    assert my_test["status_code"] == 204

