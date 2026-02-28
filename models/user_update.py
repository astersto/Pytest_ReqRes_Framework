from dataclasses import dataclass,field

@dataclass
class Data:
    id: int = 0
    email: str = ""
    first_name: str = ""
    last_name: str = ""
    avatar: str = ""

@dataclass
class Support:
    url: str = ""
    text: str = ""

@dataclass
class Cta:
    label: str = ""
    url: str = ""

@dataclass
class _Meta:
    powered_by: str = ""
    docs_url: str = ""
    upgrade_url: str = ""
    example_url: str = ""
    variant: str = ""
    message: str = ""
    context: str = ""
    cta: Cta = field(default_factory=Cta)

@dataclass
class User_Update:

    data: Data = field(default_factory=Data)
    support: Support = field(default_factory=Support)
    _meta: _Meta = field(default_factory=_Meta)

    def to_dict(self):
        return {
            "data" : {
                "id" : self.data.id,
                "email" : self.data.email,
                "first_name" : self.data.first_name,
                "last_name" : self.data.last_name,
                "avatar" : self.data.avatar
            },
            "support" : {
                "url" : self.support.url,
                "text" : self.support.text
            },
            "_meta" : {
                "powered_by" : self._meta.powered_by,
                "docs_url" : self._meta.docs_url,
                "upgrade_url" : self._meta.upgrade_url,
                "example_url" : self._meta.example_url,
                "variant" : self._meta.variant,
                "message" : self._meta.message,
                "context" : self._meta.context,
                "cta" : {
                    "label" : self._meta.cta.label,
                    "url" : self._meta.cta.url
                }
            }
        }

