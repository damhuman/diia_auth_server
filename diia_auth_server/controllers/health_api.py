import aiohttp
from aiohttp import web

from diia_auth_server.config import id_gov_ua_option
from diia_auth_server.controllers.base import BaseJsonApiController
from diia_auth_server.models.health import HealthStatus
from diia_auth_server.logger import get_logger


_logger = get_logger()


class HealthApiController(BaseJsonApiController):
    async def get(self, request: web.Request) -> web.Response:
        """
        Returns an HTTP 200 OK JSON message for clients to know the service is healthy

        Inspired by: https://tools.ietf.org/id/draft-inadarei-api-health-check-01.html

        :param request: A request that contains query params
        :return: JSON response with `{message: 'I'm alive and kicking!!!'}
        """
        # TODO: Try connecting to the database before returning "200 OK: Pass" Response
        return self.json_response(body={
            "status": HealthStatus.Pass.value
        })


class ExchangeTokensApiController(BaseJsonApiController):
    async def get(self, request: web.Request) -> web.Response:
        """
        Returns an HTTP 200 OK JSON message for clients to know the service is healthy

        Inspired by: https://tools.ietf.org/id/draft-inadarei-api-health-check-01.html

        :param request: A request that contains query params
        :return: JSON response with `{message: 'I'm alive and kicking!!!'}
        """
        code = request.data.get('code')

        exchange_token_url = f"{id_gov_ua_option('url')}/get-access-token"
        request_body = {
            "grant_type": "authorization_code",
            "client_id": id_gov_ua_option('client_id'),
            "client_secret": id_gov_ua_option('client_id'),
            "code": code
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(exchange_token_url, data=request_body) as resp:
                resp_data = await resp.json()
                _logger.info(f"Response status: {resp.status}")
                _logger.info(f"Response received: {resp_data}")

        return self.json_response(body=resp_data)
