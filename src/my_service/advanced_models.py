"""Advanced model examples using different approaches."""

from dataclasses import dataclass, field
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .models import Order


# 1. Dataclass with advanced features
@dataclass(frozen=True)  # Immutable
class ImmutableUser:
    name: str
    email: str
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class UserWithMethods:
    name: str
    email: str
    orders: List['Order'] = field(default_factory=list)
    
    @property
    def full_name(self) -> str:
        return self.name.title()
    
    def add_order(self, order: 'Order') -> None:
        self.orders.append(order)


# 2. Pydantic (install with: pip install pydantic)
# Uncomment when pydantic is installed:
"""
from pydantic import BaseModel, validator

class PydanticUser(BaseModel):
    name: str
    email: str
    age: Optional[int] = None
    
    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v
    
    class Config:
        # Enable ORM mode for database integration
        orm_mode = True
"""


# 3. NamedTuple (lightweight, immutable)
from typing import NamedTuple

class UserTuple(NamedTuple):
    name: str
    email: str
    age: Optional[int] = None


# 4. Attrs (install with: pip install attrs)
# Uncomment when attrs is installed:
"""
import attr

@attr.s(auto_attribs=True)
class AttrsUser:
    name: str
    email: str
    age: Optional[int] = None
    
    @email.validator
    def check_email(self, attribute, value):
        if '@' not in value:
            raise ValueError('Invalid email')
"""