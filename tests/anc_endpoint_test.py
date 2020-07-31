def test_anc_endpoint_apply(test_devices, test_connection):
    mac = "00:00:00:00:00:00"
    policy = "my_anc_policy"
    my_test = test_connection.anc_endpoint_apply(mac=mac, policy=policy)

    assert my_test["status_code"] == 204
