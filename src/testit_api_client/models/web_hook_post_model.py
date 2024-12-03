# coding: utf-8

"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from testit_api_client.models.request_type_model import RequestTypeModel
from testit_api_client.models.web_hook_event_type_model import WebHookEventTypeModel
from typing import Optional, Set
from typing_extensions import Self

class WebHookPostModel(BaseModel):
    """
    WebHookPostModel
    """ # noqa: E501
    project_id: StrictStr = Field(description="Unique ID of the webhook project", alias="projectId")
    event_type: WebHookEventTypeModel = Field(description="Type of event which triggers the webhook", alias="eventType")
    description: Optional[StrictStr] = Field(default=None, description="Description of the webhook")
    url: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Request URL of the webhook")
    request_type: RequestTypeModel = Field(description="Request method of the webhook", alias="requestType")
    should_send_body: StrictBool = Field(description="Indicates if the webhook sends body", alias="shouldSendBody")
    headers: Dict[str, StrictStr] = Field(description="Collection of the webhook headers")
    query_parameters: Dict[str, StrictStr] = Field(description="Collection of the webhook query parameters", alias="queryParameters")
    is_enabled: StrictBool = Field(description="Indicates if the webhook is active", alias="isEnabled")
    should_send_custom_body: StrictBool = Field(description="Indicates if the webhook sends custom body", alias="shouldSendCustomBody")
    custom_body: Optional[StrictStr] = Field(default=None, description="Custom body of the webhook", alias="customBody")
    should_replace_parameters: StrictBool = Field(description="Indicates if the webhook injects parameters", alias="shouldReplaceParameters")
    should_escape_parameters: StrictBool = Field(description="Indicates if the webhook escapes invalid characters in parameters", alias="shouldEscapeParameters")
    name: Annotated[str, Field(min_length=0, strict=True, max_length=255)] = Field(description="Name of the webhook")
    __properties: ClassVar[List[str]] = ["projectId", "eventType", "description", "url", "requestType", "shouldSendBody", "headers", "queryParameters", "isEnabled", "shouldSendCustomBody", "customBody", "shouldReplaceParameters", "shouldEscapeParameters", "name"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WebHookPostModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if custom_body (nullable) is None
        # and model_fields_set contains the field
        if self.custom_body is None and "custom_body" in self.model_fields_set:
            _dict['customBody'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebHookPostModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "projectId": obj.get("projectId"),
            "eventType": obj.get("eventType"),
            "description": obj.get("description"),
            "url": obj.get("url"),
            "requestType": obj.get("requestType"),
            "shouldSendBody": obj.get("shouldSendBody"),
            "headers": obj.get("headers"),
            "queryParameters": obj.get("queryParameters"),
            "isEnabled": obj.get("isEnabled"),
            "shouldSendCustomBody": obj.get("shouldSendCustomBody"),
            "customBody": obj.get("customBody"),
            "shouldReplaceParameters": obj.get("shouldReplaceParameters"),
            "shouldEscapeParameters": obj.get("shouldEscapeParameters"),
            "name": obj.get("name")
        })
        return _obj


