from __future__ import annotations

from typing import Any

from ..transport import AsyncTransport, Transport

class AiModule:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport

    def delete_llm_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/ai/integrations/llms/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/llms/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_llm_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/ai/integrations/llms/{Id}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/llms/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_llm_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/ai/integrations/llms/{Id}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/llms/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_llm_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/integrations/llms/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/llms/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_llm_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/integrations/llms/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/llms/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_llm_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/integrations/llms/"""
        return self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/llms/",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def test_llm_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/integrations/llms/test"""
        return self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/llms/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def delete_mcp_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/ai/integrations/mcp/{Id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/mcp/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def disable_mcp_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/ai/integrations/mcp/{Id}/disable"""
        return self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/mcp/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def enable_mcp_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/ai/integrations/mcp/{Id}/enable"""
        return self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/mcp/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_mcp_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/integrations/mcp/{id}"""
        return self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/mcp/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def get_mcp_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/integrations/mcp/integrations"""
        return self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/mcp/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def save_mcp_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/integrations/mcp/"""
        return self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/mcp/",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    def test_mcp_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/integrations/mcp/test"""
        return self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/mcp/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )


class AsyncAiModule:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def delete_llm_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/ai/integrations/llms/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/llms/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_llm_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/ai/integrations/llms/{Id}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/llms/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_llm_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/ai/integrations/llms/{Id}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/llms/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_llm_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/integrations/llms/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/llms/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_llm_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/integrations/llms/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/llms/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_llm_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/integrations/llms/"""
        return await self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/llms/",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def test_llm_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/integrations/llms/test"""
        return await self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/llms/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def delete_mcp_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """DELETE /{version}/ai/integrations/mcp/{Id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/mcp/{Id}",
            method="DELETE",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def disable_mcp_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/ai/integrations/mcp/{Id}/disable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/mcp/{Id}/disable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def enable_mcp_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """PUT /{version}/ai/integrations/mcp/{Id}/enable"""
        return await self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/mcp/{Id}/enable",
            method="PUT",
            path_params={"Id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_mcp_integration(self, id: str, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/integrations/mcp/{id}"""
        return await self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/mcp/{id}",
            method="GET",
            path_params={"id": id},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def get_mcp_integrations(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """GET /{version}/ai/integrations/mcp/integrations"""
        return await self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/mcp/integrations",
            method="GET",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def save_mcp_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/integrations/mcp/"""
        return await self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/mcp/",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )

    async def test_mcp_integration(self, *, timeout: float | None = None, bearer_token: str | None = None, **request: Any) -> Any:
        """POST /{version}/ai/integrations/mcp/test"""
        return await self._transport.send(
            target="hub",
            path="/{version}/ai/integrations/mcp/test",
            method="POST",
            path_params={},
            request=request,
            scope="project",
            timeout=timeout,
            bearer_token=bearer_token,
        )
