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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from testit_api_client.models.attachment_put_model import AttachmentPutModel
from testit_api_client.models.link_post_model import LinkPostModel
from testit_api_client.models.test_point_selector import TestPointSelector
from typing import Optional, Set
from typing_extensions import Self

class TestRunFillByConfigurationsPostModel(BaseModel):
    """
    TestRunFillByConfigurationsPostModel
    """ # noqa: E501
    test_point_selectors: List[TestPointSelector] = Field(description="Specifies an array of work items and configuration to create a test run for.", alias="testPointSelectors")
    project_id: StrictStr = Field(description="Specifies the GUID of the project, in which a test run will be created.", alias="projectId")
    test_plan_id: StrictStr = Field(description="Specifies the GUID of the test plan, within which the test run will be created.", alias="testPlanId")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the test run.")
    description: Optional[StrictStr] = Field(default=None, description="Specifies the test run description.")
    launch_source: Optional[StrictStr] = Field(default=None, description="Specifies the test run launch source.", alias="launchSource")
    attachments: Optional[List[AttachmentPutModel]] = Field(default=None, description="Collection of attachment ids to relate to the test run")
    links: Optional[List[LinkPostModel]] = Field(default=None, description="Collection of links to relate to the test run")
    __properties: ClassVar[List[str]] = ["testPointSelectors", "projectId", "testPlanId", "name", "description", "launchSource", "attachments", "links"]

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
        """Create an instance of TestRunFillByConfigurationsPostModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in test_point_selectors (list)
        _items = []
        if self.test_point_selectors:
            for _item_test_point_selectors in self.test_point_selectors:
                if _item_test_point_selectors:
                    _items.append(_item_test_point_selectors.to_dict())
            _dict['testPointSelectors'] = _items
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if launch_source (nullable) is None
        # and model_fields_set contains the field
        if self.launch_source is None and "launch_source" in self.model_fields_set:
            _dict['launchSource'] = None

        # set to None if attachments (nullable) is None
        # and model_fields_set contains the field
        if self.attachments is None and "attachments" in self.model_fields_set:
            _dict['attachments'] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestRunFillByConfigurationsPostModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "testPointSelectors": [TestPointSelector.from_dict(_item) for _item in obj["testPointSelectors"]] if obj.get("testPointSelectors") is not None else None,
            "projectId": obj.get("projectId"),
            "testPlanId": obj.get("testPlanId"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "launchSource": obj.get("launchSource"),
            "attachments": [AttachmentPutModel.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "links": [LinkPostModel.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None
        })
        return _obj


