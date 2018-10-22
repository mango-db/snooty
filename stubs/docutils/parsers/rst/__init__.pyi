import docutils.nodes
import docutils.statemachine
from typing import Any, Dict, List, Tuple


class RSTState(docutils.statemachine.State):
    def nested_parse(self, block: str, input_offset: int, node: docutils.nodes.Node) -> None: ...
    def inline_text(self, text: str, lineno: int) -> Tuple[List[docutils.nodes.Node], List[docutils.nodes.Node]]: ...


class Directive:
    arguments: List[str]
    block_text: str
    options: Any
    name: str
    content: str
    content_offset: int
    state: RSTState
    lineno: int
    state_machine: Any
    option_spec: Dict[str, object]

    def add_name(self, node: docutils.nodes.Node) -> None: ...


class Parser:
    inliner: Any
    def parse(self, data: str, document: docutils.nodes.document) -> None: ...
