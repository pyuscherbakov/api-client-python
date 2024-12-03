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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from testit_api_client.models.attachment import Attachment
from testit_api_client.models.available_test_result_outcome import AvailableTestResultOutcome
from typing import Optional, Set
from typing_extensions import Self

class AutoTestStepResult(BaseModel):
    """
    AutoTestStepResult
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="The name of the step.")
    description: Optional[StrictStr] = Field(default=None, description="Description of the step result.")
    info: Optional[StrictStr] = Field(default=None, description="Extended description of the step result.")
    started_on: Optional[datetime] = Field(default=None, description="Step start date.", alias="startedOn")
    completed_on: Optional[datetime] = Field(default=None, description="Step end date.", alias="completedOn")
    duration: Optional[Annotated[int, Field(le=43200000000, strict=True, ge=0)]] = Field(default=None, description="Expected or actual duration of the test run execution in milliseconds.")
    outcome: Optional[AvailableTestResultOutcome] = Field(default=None, description="Specifies the result of the autotest execution.")
    step_results: Optional[List[AutoTestStepResult]] = Field(default=None, description="Nested step results. The maximum nesting level is 15.", alias="stepResults")
    attachments: Optional[List[Attachment]] = Field(default=None, description="/// <summary>  Specifies an attachment GUID. Multiple values can be sent.  </summary>")
    parameters: Optional[Dict[str, StrictStr]] = Field(default=None, description="\"<b>parameter</b>\": \"<b>value</b>\" pair with arbitrary custom parameters. Multiple parameters can be sent.")
    __properties: ClassVar[List[str]] = ["title", "description", "info", "startedOn", "completedOn", "duration", "outcome", "stepResults", "attachments", "parameters"]

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
        """Create an instance of AutoTestStepResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in step_results (list)
        _items = []
        if self.step_results:
            for _item_step_results in self.step_results:
                if _item_step_results:
                    _items.append(_item_step_results.to_dict())
            _dict['stepResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if info (nullable) is None
        # and model_fields_set contains the field
        if self.info is None and "info" in self.model_fields_set:
            _dict['info'] = None

        # set to None if started_on (nullable) is None
        # and model_fields_set contains the field
        if self.started_on is None and "started_on" in self.model_fields_set:
            _dict['startedOn'] = None

        # set to None if completed_on (nullable) is None
        # and model_fields_set contains the field
        if self.completed_on is None and "completed_on" in self.model_fields_set:
            _dict['completedOn'] = None

        # set to None if duration (nullable) is None
        # and model_fields_set contains the field
        if self.duration is None and "duration" in self.model_fields_set:
            _dict['duration'] = None

        # set to None if outcome (nullable) is None
        # and model_fields_set contains the field
        if self.outcome is None and "outcome" in self.model_fields_set:
            _dict['outcome'] = None

        # set to None if step_results (nullable) is None
        # and model_fields_set contains the field
        if self.step_results is None and "step_results" in self.model_fields_set:
            _dict['stepResults'] = None

        # set to None if attachments (nullable) is None
        # and model_fields_set contains the field
        if self.attachments is None and "attachments" in self.model_fields_set:
            _dict['attachments'] = None

        # set to None if parameters (nullable) is None
        # and model_fields_set contains the field
        if self.parameters is None and "parameters" in self.model_fields_set:
            _dict['parameters'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AutoTestStepResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "description": obj.get("description"),
            "info": obj.get("info"),
            "startedOn": obj.get("startedOn"),
            "completedOn": obj.get("completedOn"),
            "duration": obj.get("duration"),
            "outcome": obj.get("outcome"),
            "stepResults": [AutoTestStepResult.from_dict(_item) for _item in obj["stepResults"]] if obj.get("stepResults") is not None else None,
            "attachments": [Attachment.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "parameters": obj.get("parameters")
        })
        return _obj

# TODO: Rewrite to not use raise_errors
AutoTestStepResult.model_rebuild(raise_errors=False)

