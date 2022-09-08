from aiohttp import web

from diia_auth_server.database import transactional_session
from diia_auth_server.models.example import Example
from diia_auth_server.controllers.base import BaseJsonApiController
from diia_auth_server.logger import get_logger


_logger = get_logger()


class ExampleApiController(BaseJsonApiController):
    """
    Example API Controller to demonstrate the out-of-the-box interaction between Aiohttp's request
    handlers and SQLAlchemy's declarative models, the async work is nicely wrapped in the database
    models functions using the `run_async` helper method which you can find at:
        `diia_auth_server.background.run_async`
    """
    async def get(self, request: web.Request) -> web.Response:
        """
        Return all Examples
        """
        async with transactional_session() as session:
            examples = await Example.get_all(session)

            return self.json_response(body=[
                example.serialized for example in examples
            ])

    async def get_by_id(self, request):
        """
        Return a single Example given its ID
        """
        example_id = request.match_info.get('id')

        async with transactional_session() as session:
            example = await Example.get_by_id(example_id, session)

            if example is None:
                return self.write_error(404, "The requested example doesn't exist!")

            return self.json_response(body=example.serialized)

