from typing import Optional

from ..ref import (
    DivisionRef
)

from ..utils import (
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
)


class PdfDetail(AppBaseModel, HrefMixin):
    """Personal Data Fields are custom fields for a card holder"""

    name: str
    server_display_name: Optional[str] = None
    description: Optional[str] = None
    division: DivisionRef
    type: str
    default: Optional[str] = None
    required: bool = False
    unique: bool = False
    default_access: str
    operator_access: Optional[str] = None
    sort_priority: int

    # access_groups

    regex: Optional[str] = None
    regex_description: Optional[str] = None
    notification_default: bool = False
    image_width: int = 0
    image_height: int = 0
    image_format: Optional[str] = None
    content_type: Optional[str] = None
    is_profile_image: bool = False
