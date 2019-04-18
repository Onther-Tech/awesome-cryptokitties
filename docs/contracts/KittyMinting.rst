
KittyMinting is KittyAuction
============================

all functions related to creating kittens.
PromoKitty, Gen0Kitty를 즉각 발행. Gen0Kitty는 즉각 경매에 올라감


Constants
---------

- ``PROMO_CREATION_LIMIT <uint256>``: Limits the number of cats the contract owner can ever create.
- ``GEN0_CREATION_LIMIT <uint256>``: Limits the number of cats the contract owner can ever create.
- ``GEN0_STARTING_PRICE <uint256>``: Constants for gen0 auctions.
- ``GEN0_AUCTION_DURATION <uint256>``: Constants for gen0 auctions.

Public State Variables
----------------------

- ``promoCreatedCount <uint256>``: Counts the number of cats the contract owner has created.
- ``gen0CreatedCount <uint256>``: Counts the number of cats the contract owner has created.


External Functions
------------------


createPromoKitty(uint256 _genes, address _owner) external onlyCOO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

we can create promo kittens, up to a limit. Only callable by COO

Parameters
""""""""""

- ``_genes <uint256>``: the encoded genes of the kitten to be created, any value is accepted
- ``_owner <address>``: the future owner of the created kittens. Default to contract COO

Returns
"""""""

None

createGen0Auction(uint256 _genes) external onlyCOO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a new gen0 kitty with the given genes and creates an auction for it.

Parameters
""""""""""

- ``_genes <uint256>``

Returns
"""""""

None
