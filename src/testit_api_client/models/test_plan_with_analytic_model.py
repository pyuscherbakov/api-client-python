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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from testit_api_client.models.tag_post_model import TagPostModel
from testit_api_client.models.test_plan_status_model import TestPlanStatusModel
from testit_api_client.models.test_point_analytic_result import TestPointAnalyticResult
from typing import Optional, Set
from typing_extensions import Self

class TestPlanWithAnalyticModel(BaseModel):
    """
    TestPlanWithAnalyticModel
    """ # noqa: E501
    analytic: TestPointAnalyticResult
    status: TestPlanStatusModel
    started_on: Optional[datetime] = Field(default=None, description="Set when test plan is starter (status changed to: In Progress)", alias="startedOn")
    completed_on: Optional[datetime] = Field(default=None, description="set when test plan status is completed (status changed to: Completed)", alias="completedOn")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    modified_date: Optional[datetime] = Field(default=None, alias="modifiedDate")
    created_by_id: StrictStr = Field(alias="createdById")
    modified_by_id: Optional[StrictStr] = Field(default=None, alias="modifiedById")
    global_id: StrictInt = Field(description="Used for search Test plan", alias="globalId")
    is_deleted: StrictBool = Field(alias="isDeleted")
    locked_date: Optional[datetime] = Field(default=None, alias="lockedDate")
    id: StrictStr
    locked_by_id: Optional[StrictStr] = Field(default=None, alias="lockedById")
    tags: Optional[List[TagPostModel]] = None
    name: Annotated[str, Field(min_length=0, strict=True, max_length=450)]
    start_date: Optional[datetime] = Field(default=None, description="Used for analytics", alias="startDate")
    end_date: Optional[datetime] = Field(default=None, description="Used for analytics", alias="endDate")
    description: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=100000)]] = None
    build: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=450)]] = None
    project_id: StrictStr = Field(alias="projectId")
    product_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=450)]] = Field(default=None, alias="productName")
    has_automatic_duration_timer: Optional[StrictBool] = Field(default=None, alias="hasAutomaticDurationTimer")
    attributes: Dict[str, Any]
    __properties: ClassVar[List[str]] = ["analytic", "status", "startedOn", "completedOn", "createdDate", "modifiedDate", "createdById", "modifiedById", "globalId", "isDeleted", "lockedDate", "id", "lockedById", "tags", "name", "startDate", "endDate", "description", "build", "projectId", "productName", "hasAutomaticDurationTimer", "attributes"]

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
        """Create an instance of TestPlanWithAnalyticModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of analytic
        if self.analytic:
            _dict['analytic'] = self.analytic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        # set to None if started_on (nullable) is None
        # and model_fields_set contains the field
        if self.started_on is None and "started_on" in self.model_fields_set:
            _dict['startedOn'] = None

        # set to None if completed_on (nullable) is None
        # and model_fields_set contains the field
        if self.completed_on is None and "completed_on" in self.model_fields_set:
            _dict['completedOn'] = None

        # set to None if created_date (nullable) is None
        # and model_fields_set contains the field
        if self.created_date is None and "created_date" in self.model_fields_set:
            _dict['createdDate'] = None

        # set to None if modified_date (nullable) is None
        # and model_fields_set contains the field
        if self.modified_date is None and "modified_date" in self.model_fields_set:
            _dict['modifiedDate'] = None

        # set to None if modified_by_id (nullable) is None
        # and model_fields_set contains the field
        if self.modified_by_id is None and "modified_by_id" in self.model_fields_set:
            _dict['modifiedById'] = None

        # set to None if locked_date (nullable) is None
        # and model_fields_set contains the field
        if self.locked_date is None and "locked_date" in self.model_fields_set:
            _dict['lockedDate'] = None

        # set to None if locked_by_id (nullable) is None
        # and model_fields_set contains the field
        if self.locked_by_id is None and "locked_by_id" in self.model_fields_set:
            _dict['lockedById'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if start_date (nullable) is None
        # and model_fields_set contains the field
        if self.start_date is None and "start_date" in self.model_fields_set:
            _dict['startDate'] = None

        # set to None if end_date (nullable) is None
        # and model_fields_set contains the field
        if self.end_date is None and "end_date" in self.model_fields_set:
            _dict['endDate'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if build (nullable) is None
        # and model_fields_set contains the field
        if self.build is None and "build" in self.model_fields_set:
            _dict['build'] = None

        # set to None if product_name (nullable) is None
        # and model_fields_set contains the field
        if self.product_name is None and "product_name" in self.model_fields_set:
            _dict['productName'] = None

        # set to None if has_automatic_duration_timer (nullable) is None
        # and model_fields_set contains the field
        if self.has_automatic_duration_timer is None and "has_automatic_duration_timer" in self.model_fields_set:
            _dict['hasAutomaticDurationTimer'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestPlanWithAnalyticModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "analytic": TestPointAnalyticResult.from_dict(obj["analytic"]) if obj.get("analytic") is not None else None,
            "status": obj.get("status"),
            "startedOn": obj.get("startedOn"),
            "completedOn": obj.get("completedOn"),
            "createdDate": obj.get("createdDate"),
            "modifiedDate": obj.get("modifiedDate"),
            "createdById": obj.get("createdById"),
            "modifiedById": obj.get("modifiedById"),
            "globalId": obj.get("globalId"),
            "isDeleted": obj.get("isDeleted"),
            "lockedDate": obj.get("lockedDate"),
            "id": obj.get("id"),
            "lockedById": obj.get("lockedById"),
            "tags": [TagPostModel.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "name": obj.get("name"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "description": obj.get("description"),
            "build": obj.get("build"),
            "projectId": obj.get("projectId"),
            "productName": obj.get("productName"),
            "hasAutomaticDurationTimer": obj.get("hasAutomaticDurationTimer"),
            "attributes": obj.get("attributes")
        })
        return _obj


