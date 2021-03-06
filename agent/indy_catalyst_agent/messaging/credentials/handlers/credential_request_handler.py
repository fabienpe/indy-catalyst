"""Credential request handler."""

from ...base_handler import BaseHandler, BaseResponder, HandlerException, RequestContext


from ..manager import CredentialManager
from ..messages.credential_request import CredentialRequest


class CredentialRequestHandler(BaseHandler):
    """Message handler class for credential requests."""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """
        Message handler logic for credential requests.

        Args:
            context: request context
            responder: responder callback
        """
        self._logger.debug(f"CredentialRequestHandler called with context {context}")

        assert isinstance(context.message, CredentialRequest)

        self._logger.info(
            "Received credential request: %s", context.message.serialize(as_string=True)
        )

        if not context.connection_active:
            raise HandlerException("No connection established for credential request")

        credential_manager = CredentialManager(context)
        await credential_manager.receive_request(context.message)
