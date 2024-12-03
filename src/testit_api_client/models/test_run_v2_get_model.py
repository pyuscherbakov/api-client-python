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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from testit_api_client.models.attachment_model import AttachmentModel
from testit_api_client.models.link_model import LinkModel
from testit_api_client.models.named_entity_model import NamedEntityModel
from testit_api_client.models.test_result_v2_get_model import TestResultV2GetModel
from testit_api_client.models.test_run_state import TestRunState
from typing import Optional, Set
from typing_extensions import Self

class TestRunV2GetModel(BaseModel):
    """
    TestRunV2GetModel
    """ # noqa: E501
    started_on: Optional[datetime] = Field(default=None, alias="startedOn")
    completed_on: Optional[datetime] = Field(default=None, alias="completedOn")
    state_name: TestRunState = Field(alias="stateName")
    project_id: StrictStr = Field(description="This property is used to link test run with project", alias="projectId")
    test_plan_id: Optional[StrictStr] = Field(default=None, description="This property is used to link test run with test plan", alias="testPlanId")
    test_results: Optional[List[TestResultV2GetModel]] = Field(default=None, alias="testResults")
    created_date: datetime = Field(alias="createdDate")
    modified_date: Optional[datetime] = Field(default=None, alias="modifiedDate")
    created_by_id: StrictStr = Field(alias="createdById")
    modified_by_id: Optional[StrictStr] = Field(default=None, alias="modifiedById")
    created_by_user_name: Optional[StrictStr] = Field(default=None, alias="createdByUserName")
    attachments: List[AttachmentModel]
    links: List[LinkModel]
    custom_parameters: Optional[Dict[str, StrictStr]] = Field(default=None, alias="customParameters")
    webhooks: List[NamedEntityModel]
    run_count: StrictInt = Field(alias="runCount")
    id: StrictStr
    name: Annotated[str, Field(min_length=1, strict=True)]
    description: Optional[StrictStr] = None
    launch_source: Optional[StrictStr] = Field(default=None, description="Once launch source is specified it cannot be updated", alias="launchSource")
    __properties: ClassVar[List[str]] = ["startedOn", "completedOn", "stateName", "projectId", "testPlanId", "testResults", "createdDate", "modifiedDate", "createdById", "modifiedById", "createdByUserName", "attachments", "links", "customParameters", "webhooks", "runCount", "id", "name", "description", "launchSource"]

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
        """Create an instance of TestRunV2GetModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in test_results (list)
        _items = []
        if self.test_results:
            for _item_test_results in self.test_results:
                if _item_test_results:
                    _items.append(_item_test_results.to_dict())
            _dict['testResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item_links in self.links:
                if _item_links:
                    _items.append(_item_links.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in webhooks (list)
        _items = []
        if self.webhooks:
            for _item_webhooks in self.webhooks:
                if _item_webhooks:
                    _items.append(_item_webhooks.to_dict())
            _dict['webhooks'] = _items
        # set to None if started_on (nullable) is None
        # and model_fields_set contains the field
        if self.started_on is None and "started_on" in self.model_fields_set:
            _dict['startedOn'] = None

        # set to None if completed_on (nullable) is None
        # and model_fields_set contains the field
        if self.completed_on is None and "completed_on" in self.model_fields_set:
            _dict['completedOn'] = None

        # set to None if test_plan_id (nullable) is None
        # and model_fields_set contains the field
        if self.test_plan_id is None and "test_plan_id" in self.model_fields_set:
            _dict['testPlanId'] = None

        # set to None if test_results (nullable) is None
        # and model_fields_set contains the field
        if self.test_results is None and "test_results" in self.model_fields_set:
            _dict['testResults'] = None

        # set to None if modified_date (nullable) is None
        # and model_fields_set contains the field
        if self.modified_date is None and "modified_date" in self.model_fields_set:
            _dict['modifiedDate'] = None

        # set to None if modified_by_id (nullable) is None
        # and model_fields_set contains the field
        if self.modified_by_id is None and "modified_by_id" in self.model_fields_set:
            _dict['modifiedById'] = None

        # set to None if created_by_user_name (nullable) is None
        # and model_fields_set contains the field
        if self.created_by_user_name is None and "created_by_user_name" in self.model_fields_set:
            _dict['createdByUserName'] = None

        # set to None if custom_parameters (nullable) is None
        # and model_fields_set contains the field
        if self.custom_parameters is None and "custom_parameters" in self.model_fields_set:
            _dict['customParameters'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if launch_source (nullable) is None
        # and model_fields_set contains the field
        if self.launch_source is None and "launch_source" in self.model_fields_set:
            _dict['launchSource'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestRunV2GetModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "startedOn": obj.get("startedOn"),
            "completedOn": obj.get("completedOn"),
            "stateName": obj.get("stateName"),
            "projectId": obj.get("projectId"),
            "testPlanId": obj.get("testPlanId"),
            "testResults": [TestResultV2GetModel.from_dict(_item) for _item in obj["testResults"]] if obj.get("testResults") is not None else None,
            "createdDate": obj.get("createdDate"),
            "modifiedDate": obj.get("modifiedDate"),
            "createdById": obj.get("createdById"),
            "modifiedById": obj.get("modifiedById"),
            "createdByUserName": obj.get("createdByUserName"),
            "attachments": [AttachmentModel.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "links": [LinkModel.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "customParameters": obj.get("customParameters"),
            "webhooks": [NamedEntityModel.from_dict(_item) for _item in obj["webhooks"]] if obj.get("webhooks") is not None else None,
            "runCount": obj.get("runCount"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "launchSource": obj.get("launchSource")
        })
        return _obj


