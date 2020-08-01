class TestANCPolicy:
    def test_create_anc_policy(test_devices, test_connection_anc_policy):
        pass

    def test_update_anc_policy(test_devices, test_connection_anc_policy):
        pass

    def test_get_all_anc_policies(test_connection_anc_policy):
        pass

    def test_get_anc_policy_by_name(test_devices, test_connection_anc_policy):
        pass

    def test_get_anc_policy_by_id(test_devices, test_connection_anc_policy):
        pass

    def test_get_anc_policy_version(test_connection_anc_policy):
        pass

    def test_delete_anc_policy(test_devices, test_connection_anc_policy):
        pass


class TestANCEndpoint:
    def test_anc_endpoint_apply(test_devices, test_connection_anc_endpoints):
        mac = "00:00:00:00:00:00"
        policy = "my_anc_policy"
        my_test = test_connection_anc_endpoints.anc_endpoint_apply(
            mac=mac, policy=policy
        )
        assert my_test["status_code"] == 204

    def test_get_anc_endpoint_by_id(test_devices, test_connection_anc_endpoints):
        pass

    def test_get_all_anc_endpoints(test_connection_anc_endpoints):
        pass

    def test_get_anc_endpoint_version(test_connection_anc_endpoints):
        pass

    def test_anc_endpoint_clear(test_devices, test_connection_anc_endpoints):
        pass
