class TestANCPolicy:
    def test_create_anc_policy(self, test_connection_anc_policy):
        name = "my_anc_policy"
        actions = "QUARANTINE"
        my_test = test_connection_anc_policy.create_anc_policy(
            name=name, actions=actions
        )
        assert my_test["status_code"] == 201

    def test_update_anc_policy(self, test_connection_anc_policy):
        id = "my_anc_policy"
        actions = "SHUTDOWN"
        my_test = test_connection_anc_policy.update_anc_policy(id=id, actions=actions)

        assert (
            my_test["json"]["UpdatedFieldsList"]["updatedField"][0]["newValue"]
            == "SHUT_DOWN"
        )

    def test_get_all_anc_policies(self, test_connection_anc_policy):
        my_test = test_connection_anc_policy.get_all_anc_policies()

        assert my_test["status_code"] == 200

    def test_get_anc_policy_by_name(self, test_connection_anc_policy):
        name = "my_anc_policy"

        my_test = test_connection_anc_policy.get_anc_policy_by_name(name=name)
        assert my_test["status_code"] == 200

    def test_get_anc_policy_by_id(self, test_connection_anc_policy):
        id = "my_anc_policy"

        my_test = test_connection_anc_policy.get_anc_policy_by_id(id=id)
        assert my_test["status_code"] == 200

    def test_get_anc_policy_version(self, test_connection_anc_policy):
        my_test = test_connection_anc_policy.get_anc_policy_version()

        assert my_test["status_code"] == 200

    def test_delete_anc_policy(self, test_connection_anc_policy):
        id = "my_anc_policy"

        my_test = test_connection_anc_policy.delete_anc_policy(id=id)

        assert my_test["status_code"] == 204


class TestANCEndpoint:
    def test_anc_endpoint_apply(self, test_connection_anc_endpoints):
        mac = "00:00:00:00:00:00"
        policy = "my_anc_policy"
        my_test = test_connection_anc_endpoints.anc_endpoint_apply(
            mac=mac, policy=policy
        )
        assert my_test["status_code"] == 204

    def test_get_anc_endpoint_by_id(self, test_connection_anc_endpoints):
        my_test = test_connection_anc_endpoints.get_anc_endpoint_by_id(
            id="00:00:00:00:00:00"
        )

        assert my_test["status_code"] == 200

    def test_get_all_anc_endpoints(self, test_connection_anc_endpoints):
        my_test = test_connection_anc_endpoints.get_all_anc_endpoints()

        assert my_test["status_code"] == 200

    def test_get_anc_endpoint_version(self, test_connection_anc_endpoints):
        my_test = test_connection_anc_endpoints.get_anc_endpoint_version()

        assert my_test["status_code"] == 200

    def test_anc_endpoint_clear(self, test_connection_anc_endpoints):
        my_test = test_connection_anc_endpoints.anc_endpoint_clear(
            mac="00:00:00:00:00:00"
        )
