
KittyBreeding is KittyOwnership
===============================

A facet of KittyCore that manages Kitty siring, gestation, and birth.



Public State Variables
----------------------

- ``autoBirthFee <uint256>``: The minimum payment required to use breedWithAuto(). This fee goes towards the gas cost paid by whatever calls giveBirth(), and can be dynamically updated by the COO role as the gas price changes.
- ``pregnantKitties <uint256>``: Keeps track of number of pregnant kitties.
- ``geneScience <GeneScienceInterface>``: The address of the sibling contract that is used to implement the sooper-sekret genetic combination algorithm.

Events
------

Pregnant(address owner, uint256 matronId, uint256 sireId, uint256 cooldownEndBlock)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Pregnant event is fired when two cats successfully breed and the pregnancy timer begins for the matron.

Parameters
""""""""""

- ``owner <address>``
- ``matronId <uint256>``
- ``sireId <uint256>``
- ``cooldownEndBlock <uint256>``

External Functions
------------------


setGeneScienceAddress(address _address) external onlyCEO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update the address of the genetic contract, can only be called by the CEO.

Parameters
""""""""""

- ``_address <address>``: An address of a GeneScience contract instance to be used from this point forward.

Returns
"""""""

None

setAutoBirthFee(uint256 val) external onlyCOO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates the minimum payment required for calling giveBirthAuto(). Can only be called by the COO address. (This fee is used to offset the gas cost incurred by the autobirth daemon).

Parameters
""""""""""

- ``val <uint256>``

Returns
"""""""

None

approveSiring(address _addr, uint256 _sireId)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Grants approval to another user to sire with one of your Kitties.

Parameters
""""""""""

- ``_addr <address>``: The address that will be able to sire with your Kitty. Set to address(0) to clear all siring approvals for this Kitty.
- ``_sireId <uint256>``: A Kitty that you own that _addr will now be able to sire with.

Returns
"""""""

None

isReadyToBreed(uint256 _kittyId) public view returns (bool)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks that a given kitten is able to breed (i.e. it is not pregnant or in the middle of a siring cooldown).

Parameters
""""""""""

- ``_kittyId <uint256>``: reference the id of the kitten, any user can inquire about it

Returns
"""""""

- ``<bool>``

isPregnant(uint256 _kittyId) public view returns (bool)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a kitty is currently pregnant.

Parameters
""""""""""

- ``_kittyId <uint256>``: reference the id of the kitten, any user can inquire about it

Returns
"""""""

- ``<bool>``

canBreedWith(uint256 _matronId, uint256 _sireId) external view returns (bool)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks to see if two cats can breed together, including checks for ownership and siring approvals. Does NOT check that both cats are ready for breeding (i.e. breedWith could still fail until the cooldowns are finished).

Parameters
""""""""""

- ``_matronId <uint256>``: The ID of the proposed matron.
- ``_sireId <uint256>``: The ID of the proposed sire.

Returns
"""""""

- ``<bool>``

breedWithAuto(uint256 _matronId, uint256 _sireId) external payable whenNotPaused
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Breed a Kitty you own (as matron) with a sire that you own, or for which you have previously been given Siring approval. Will either make your cat pregnant, or will fail entirely. Requires a pre-payment of the fee given out to the first caller of giveBirth()

Parameters
""""""""""

- ``_matronId <uint256>``: The ID of the Kitty acting as matron (will end up pregnant if successful)
- ``_sireId <uint256>``: The ID of the Kitty acting as sire (will begin its siring cooldown if successful)

Returns
"""""""

None

giveBirth(uint256 _matronId) external payable whenNotPaused
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Have a pregnant Kitty give birth!
Looks at a given Kitty and, if pregnant and if the gestation period has passed, combines the genes of the two parents to create a new kitten. The new Kitty is assigned to the current owner of the matron. Upon successful completion, both the matron and the new kitten will be ready to breed again. Note that anyone can call this function (if they are willing to pay the gas!), but the new kitten always goes to the mother's owner.

Parameters
""""""""""

- ``_matronId <uint256>``: A Kitty ready to give birth.

Returns
"""""""

- ``<uint256>``: The Kitty ID of the new kitten.
