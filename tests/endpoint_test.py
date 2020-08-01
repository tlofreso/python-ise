class TestEndpointGroups:
    def test_get_all_endpoint_groups(self, test_connection_endpoint_groups):
        my_test = test_connection_endpoint_groups.get_all_endpoint_groups()

        assert my_test["json"]["SearchResult"]["total"] > 0
        assert my_test["status_code"] == 200

    def test_get_endpoint_group_by_name(
        self, test_devices, test_connection_endpoint_groups
    ):
        group = test_devices[0][1]
        my_test = test_connection_endpoint_groups.get_endpoint_group_by_name(
            group_name=group
        )

        assert my_test["json"]["SearchResult"]["resources"][0]["name"] == group


class TestEndpoints:
    def test_create_endpoint(self, test_devices, test_connection_endpoints):
        mac = test_devices[0][0]
        group = test_devices[0][1]
        desc = test_devices[0][2]
        my_test = test_connection_endpoints.create_endpoint(
            mac=mac, group_name=group, description=desc
        )

        assert my_test["status_code"] == 201

    def test_get_all_endpoints(self, test_connection_endpoints):
        my_test = test_connection_endpoints.get_all_endpoints()

        assert my_test["json"]["SearchResult"]["total"] > 0
        assert my_test["status_code"] == 200

    def test_get_endpoint_by_id(self, test_connection_endpoints):
        result = test_connection_endpoints.get_all_endpoints()
        endpoint_id = result["json"]["SearchResult"]["resources"][0]["id"]
        my_test = test_connection_endpoints.get_endpoint_by_id(id=endpoint_id)

        assert my_test["status_code"] == 200
        assert my_test["json"]["ERSEndPoint"]["id"] == endpoint_id

    def test_get_rejected_endpoints(self, test_connection_endpoints):
        my_test = test_connection_endpoints.get_rejected_endpoints()

        assert my_test["status_code"] == 200

    def test_get_endpoint_version_info(self, test_connection_endpoints):
        my_test = test_connection_endpoints.get_endpoint_version_info()

        assert "VersionInfo" in my_test["json"]

    def test_update_endpoint(self, test_devices, test_connection_endpoints):
        mac = test_devices[0][0]
        group = test_devices[0][1]
        desc = test_devices[0][2]
        my_test = test_connection_endpoints.update_endpoint(
            mac=mac, group_name=group, description=desc, endpoint_name="AdamsPhone"
        )

        assert my_test["status_code"] == 200

    def test_get_endpoint_by_mac(self, test_devices, test_connection_endpoints):
        my_test = test_connection_endpoints.get_endpoint_by_mac(test_devices[0][0])

        assert (
            my_test["status_code"] == 200
            and my_test["json"]["SearchResult"]["total"] == 1
        )

    def test_get_endpoint_by_name(self, test_devices, test_connection_endpoints):
        my_test = test_connection_endpoints.get_endpoint_by_name(test_devices[0][0])

        assert (
            my_test["status_code"] == 200 and my_test["json"]["ERSEndPoint"] is not None
        )

    def test_delete_endpoint(self, test_devices, test_connection_endpoints):
        mac = test_devices[0][0]
        my_test = test_connection_endpoints.delete_endpoint(mac=mac)

        assert my_test["status_code"] == 204

