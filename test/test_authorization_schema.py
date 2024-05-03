# coding: utf-8

"""
    Gravscale Public Restful API

    API pública da Gravscale oferece aos usuários a capacidade de se autenticar, visualizar e contratar produtos disponíveis, enviar dados de contratação, escolher formas de pagamento e gerenciar nossos produtos. Além disso, os usuários podem cadastrar chaves SSH e realizar o deploy de um sistema operacional de forma eficiente e segura. Esta API foi projetado para simplificar e agilizar o gerenciamento de recursos proporcionando que a a Gravscale forneça uma experiência integrada e intuitiva para os usuários.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gravscale.models.authorization_schema import AuthorizationSchema

class TestAuthorizationSchema(unittest.TestCase):
    """AuthorizationSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthorizationSchema:
        """Test AuthorizationSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthorizationSchema`
        """
        model = AuthorizationSchema()
        if include_optional:
            return AuthorizationSchema(
                access_token = '',
                type = ''
            )
        else:
            return AuthorizationSchema(
                access_token = '',
                type = '',
        )
        """

    def testAuthorizationSchema(self):
        """Test AuthorizationSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
