# coding: utf-8

"""
    Gravscale Public Restful API

    API pública da Gravscale oferece aos usuários a capacidade de se autenticar, visualizar e contratar produtos disponíveis, enviar dados de contratação, escolher formas de pagamento e gerenciar nossos produtos. Além disso, os usuários podem cadastrar chaves SSH e realizar o deploy de um sistema operacional de forma eficiente e segura. Esta API foi projetado para simplificar e agilizar o gerenciamento de recursos proporcionando que a a Gravscale forneça uma experiência integrada e intuitiva para os usuários.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gravscale.api.account_api import AccountApi


class TestAccountApi(unittest.TestCase):
    """AccountApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccountApi()

    def tearDown(self) -> None:
        pass

    def test_get_account(self) -> None:
        """Test case for get_account

        Get Account
        """
        pass

    def test_list_accounts(self) -> None:
        """Test case for list_accounts

        List All Accounts
        """
        pass


if __name__ == "__main__":
    unittest.main()
