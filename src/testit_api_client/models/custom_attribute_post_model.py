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
from typing_extensions import Annotated
from testit_api_client.models.custom_attribute_option_post_model import CustomAttributeOptionPostModel
from testit_api_client.models.custom_attribute_types_enum import CustomAttributeTypesEnum
from typing import Optional, Set
from typing_extensions import Self

class CustomAttributePostModel(BaseModel):
    """
    CustomAttributePostModel
    """ # noqa: E501
    options: Optional[List[CustomAttributeOptionPostModel]] = Field(default=None, description="Collection of attribute options     Available for attributes of type `options` and `multiple options` only")
    type: CustomAttributeTypesEnum = Field(description="Type of attribute")
    name: Annotated[str, Field(min_length=0, strict=True, max_length=255)] = Field(description="Name of the attribute")
    is_enabled: StrictBool = Field(description="Indicates if the attribute is enabled", alias="isEnabled")
    is_required: StrictBool = Field(description="Indicates if the attribute value is mandatory to specify", alias="isRequired")
    is_global: StrictBool = Field(description="Indicates if the attribute is available across all projects", alias="isGlobal")
    __properties: ClassVar[List[str]] = ["options", "type", "name", "isEnabled", "isRequired", "isGlobal"]

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
        """Create an instance of CustomAttributePostModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item_options in self.options:
                if _item_options:
                    _items.append(_item_options.to_dict())
            _dict['options'] = _items
        # set to None if options (nullable) is None
        # and model_fields_set contains the field
        if self.options is None and "options" in self.model_fields_set:
            _dict['options'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomAttributePostModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "options": [CustomAttributeOptionPostModel.from_dict(_item) for _item in obj["options"]] if obj.get("options") is not None else None,
            "type": obj.get("type"),
            "name": obj.get("name"),
            "isEnabled": obj.get("isEnabled"),
            "isRequired": obj.get("isRequired"),
            "isGlobal": obj.get("isGlobal")
        })
        return _obj


