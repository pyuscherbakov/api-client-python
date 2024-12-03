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
from testit_api_client.models.auto_test_step_model import AutoTestStepModel
from testit_api_client.models.label_post_model import LabelPostModel
from testit_api_client.models.link_put_model import LinkPutModel
from typing import Optional, Set
from typing_extensions import Self

class AutoTestPutModel(BaseModel):
    """
    AutoTestPutModel
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Used for search autotest. If value is null or equals Guid mask filled with zeros, search will be executed using ExternalId")
    work_item_ids_for_link_with_auto_test: Optional[List[StrictStr]] = Field(default=None, alias="workItemIdsForLinkWithAutoTest")
    external_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="External ID of the autotest", alias="externalId")
    links: Optional[List[LinkPutModel]] = Field(default=None, description="Collection of the autotest links")
    project_id: StrictStr = Field(description="Unique ID of the autotest project", alias="projectId")
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Name of the autotest")
    namespace: Optional[StrictStr] = Field(default=None, description="Name of the autotest namespace")
    classname: Optional[StrictStr] = Field(default=None, description="Name of the autotest class")
    steps: Optional[List[AutoTestStepModel]] = Field(default=None, description="Collection of the autotest steps")
    setup: Optional[List[AutoTestStepModel]] = Field(default=None, description="Collection of the autotest setup steps")
    teardown: Optional[List[AutoTestStepModel]] = Field(default=None, description="Collection of the autotest teardown steps")
    title: Optional[StrictStr] = Field(default=None, description="Name of the autotest in autotest's card")
    description: Optional[StrictStr] = Field(default=None, description="Description of the autotest in autotest's card")
    labels: Optional[List[LabelPostModel]] = Field(default=None, description="Collection of the autotest labels")
    is_flaky: Optional[StrictBool] = Field(default=None, description="Indicates if the autotest is marked as flaky", alias="isFlaky")
    external_key: Optional[StrictStr] = Field(default=None, description="External key of the autotest", alias="externalKey")
    __properties: ClassVar[List[str]] = ["id", "workItemIdsForLinkWithAutoTest", "externalId", "links", "projectId", "name", "namespace", "classname", "steps", "setup", "teardown", "title", "description", "labels", "isFlaky", "externalKey"]

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
        """Create an instance of AutoTestPutModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item_links in self.links:
                if _item_links:
                    _items.append(_item_links.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item_steps in self.steps:
                if _item_steps:
                    _items.append(_item_steps.to_dict())
            _dict['steps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in setup (list)
        _items = []
        if self.setup:
            for _item_setup in self.setup:
                if _item_setup:
                    _items.append(_item_setup.to_dict())
            _dict['setup'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in teardown (list)
        _items = []
        if self.teardown:
            for _item_teardown in self.teardown:
                if _item_teardown:
                    _items.append(_item_teardown.to_dict())
            _dict['teardown'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item_labels in self.labels:
                if _item_labels:
                    _items.append(_item_labels.to_dict())
            _dict['labels'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if work_item_ids_for_link_with_auto_test (nullable) is None
        # and model_fields_set contains the field
        if self.work_item_ids_for_link_with_auto_test is None and "work_item_ids_for_link_with_auto_test" in self.model_fields_set:
            _dict['workItemIdsForLinkWithAutoTest'] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict['links'] = None

        # set to None if namespace (nullable) is None
        # and model_fields_set contains the field
        if self.namespace is None and "namespace" in self.model_fields_set:
            _dict['namespace'] = None

        # set to None if classname (nullable) is None
        # and model_fields_set contains the field
        if self.classname is None and "classname" in self.model_fields_set:
            _dict['classname'] = None

        # set to None if steps (nullable) is None
        # and model_fields_set contains the field
        if self.steps is None and "steps" in self.model_fields_set:
            _dict['steps'] = None

        # set to None if setup (nullable) is None
        # and model_fields_set contains the field
        if self.setup is None and "setup" in self.model_fields_set:
            _dict['setup'] = None

        # set to None if teardown (nullable) is None
        # and model_fields_set contains the field
        if self.teardown is None and "teardown" in self.model_fields_set:
            _dict['teardown'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if labels (nullable) is None
        # and model_fields_set contains the field
        if self.labels is None and "labels" in self.model_fields_set:
            _dict['labels'] = None

        # set to None if is_flaky (nullable) is None
        # and model_fields_set contains the field
        if self.is_flaky is None and "is_flaky" in self.model_fields_set:
            _dict['isFlaky'] = None

        # set to None if external_key (nullable) is None
        # and model_fields_set contains the field
        if self.external_key is None and "external_key" in self.model_fields_set:
            _dict['externalKey'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AutoTestPutModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "workItemIdsForLinkWithAutoTest": obj.get("workItemIdsForLinkWithAutoTest"),
            "externalId": obj.get("externalId"),
            "links": [LinkPutModel.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "projectId": obj.get("projectId"),
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "classname": obj.get("classname"),
            "steps": [AutoTestStepModel.from_dict(_item) for _item in obj["steps"]] if obj.get("steps") is not None else None,
            "setup": [AutoTestStepModel.from_dict(_item) for _item in obj["setup"]] if obj.get("setup") is not None else None,
            "teardown": [AutoTestStepModel.from_dict(_item) for _item in obj["teardown"]] if obj.get("teardown") is not None else None,
            "title": obj.get("title"),
            "description": obj.get("description"),
            "labels": [LabelPostModel.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None,
            "isFlaky": obj.get("isFlaky"),
            "externalKey": obj.get("externalKey")
        })
        return _obj


