
KittyAccessControl is Pausable
==============================

A facet of KittyCore that manages special access privileges.



Public State Variables
----------------------

- ``ceoAddress <address>``
- ``cfoAddress <address>``
- ``cooAddress <address>``


External Functions
------------------


setCEO(address _newCEO) external onlyCEO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assigns a new address to act as the CEO. Only available to the current CEO.

Parameters
""""""""""

- ``_newCEO <address>``: The address of the new CEO

Returns
"""""""

None

setCFO(address _newCFO) external onlyCEO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assigns a new address to act as the CFO. Only available to the current CEO.

Parameters
""""""""""

- ``_newCFO <address>``: The address of the new CFO

Returns
"""""""

None

setCOO(address _newCOO) external onlyCEO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assigns a new address to act as the COO. Only available to the current CEO.

Parameters
""""""""""

- ``_newCOO <address>``: The address of the new COO

Returns
"""""""

None
