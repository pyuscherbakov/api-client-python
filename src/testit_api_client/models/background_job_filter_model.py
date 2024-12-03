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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from testit_api_client.models.background_job_state import BackgroundJobState
from testit_api_client.models.background_job_type import BackgroundJobType
from testit_api_client.models.date_time_range_selector_model import DateTimeRangeSelectorModel
from typing import Optional, Set
from typing_extensions import Self

class BackgroundJobFilterModel(BaseModel):
    """
    BackgroundJobFilterModel
    """ # noqa: E501
    types: Optional[List[BackgroundJobType]] = None
    states: Optional[List[BackgroundJobState]] = None
    is_deleted: Optional[StrictBool] = Field(default=None, alias="isDeleted")
    start_date: Optional[DateTimeRangeSelectorModel] = Field(default=None, alias="startDate")
    end_date: Optional[DateTimeRangeSelectorModel] = Field(default=None, alias="endDate")
    __properties: ClassVar[List[str]] = ["types", "states", "isDeleted", "startDate", "endDate"]

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
        """Create an instance of BackgroundJobFilterModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of start_date
        if self.start_date:
            _dict['startDate'] = self.start_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_date
        if self.end_date:
            _dict['endDate'] = self.end_date.to_dict()
        # set to None if types (nullable) is None
        # and model_fields_set contains the field
        if self.types is None and "types" in self.model_fields_set:
            _dict['types'] = None

        # set to None if states (nullable) is None
        # and model_fields_set contains the field
        if self.states is None and "states" in self.model_fields_set:
            _dict['states'] = None

        # set to None if is_deleted (nullable) is None
        # and model_fields_set contains the field
        if self.is_deleted is None and "is_deleted" in self.model_fields_set:
            _dict['isDeleted'] = None

        # set to None if start_date (nullable) is None
        # and model_fields_set contains the field
        if self.start_date is None and "start_date" in self.model_fields_set:
            _dict['startDate'] = None

        # set to None if end_date (nullable) is None
        # and model_fields_set contains the field
        if self.end_date is None and "end_date" in self.model_fields_set:
            _dict['endDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BackgroundJobFilterModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "types": obj.get("types"),
            "states": obj.get("states"),
            "isDeleted": obj.get("isDeleted"),
            "startDate": DateTimeRangeSelectorModel.from_dict(obj["startDate"]) if obj.get("startDate") is not None else None,
            "endDate": DateTimeRangeSelectorModel.from_dict(obj["endDate"]) if obj.get("endDate") is not None else None
        })
        return _obj


