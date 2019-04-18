
KittyBase is KittyAccessControl
===============================

Base contract for CryptoKitties. Holds all common structs, events and base variables.

두 키티를 breeding해 새로운 키티를 생성할 때 kittyId가 sequeutnal increment하게 생성됨. Requetable하기 위해서 랜덤하게 생성되도록 변경되어야 함

Struct
------

Kitty
^^^^^

The main Kitty struct. Every cat in CryptoKitties is represented by a copy of this structure, so great care was taken to ensure that it fits neatly into exactly two 256-bit words. Note that the order of the members in this structure is important because of the byte-packing rules used by Ethereum. 
Ref: http://solidity.readthedocs.io/en/develop/miscellaneous.html

Members
"""""""
- ``genes <uint256>``: The Kitty's genetic code is packed into these 256-bits, the format is sooper-sekret! A cat's genes never change.
- ``birthTime <uint64>``: birthTime
- ``cooldownEndBlock <uint64>``: The minimum timestamp after which this cat can engage in breeding activities again. This same timestamp is used for the pregnancy timer (for matrons) as well as the siring cooldown.
- ``matronId <uint32>``: The ID of the parents of this kitty, set to 0 for gen0 cats. Note that using 32-bit unsigned integers limits us to a "mere" 4 billion cats. This number might seem small until you realize that Ethereum currently has a limit of about 500 million transactions per year! So, this definitely won't be a problem for several years (even as Ethereum learns to scale).
- ``sireId <uint32>``: Same as ``matronId``
- ``siringWithId <uint32>``: Set to the ID of the sire cat for matrons that are pregnant, zero otherwise. A non-zero value here is how we know a cat is pregnant. Used to retrieve the genetic material for the new kitten when the birth transpires.
- ``cooldownIndex <uint16>``: Set to the index in the cooldown array (see below) that represents the current cooldown duration for this Kitty. This starts at zero for gen0 cats, and is initialized to floor(generation/2) for others. Incremented by one for each successful breeding action, regardless of whether this cat is acting as matron or sire.
- ``generation <uint16>``: The "generation number" of this cat. Cats minted by the CK contract for sale are called "gen0" and have a generation number of 0. The generation number of all other cats is the larger of the two generation numbers of their parents, plus one. 
i.e. max(matron.generation, sire.generation) + 1)


Public State Variables
----------------------

- ``cooldowns <uint32[14]>``: A lookup table indicating the cooldown duration after any successful breeding action, called "pregnancy time" for matrons and "siring cooldown" for sires. Designed such that the cooldown roughly doubles each time a cat is bred, encouraging owners not to just keep breeding the same cat over and over again. Caps out at one week (a cat can breed an unbounded number of times, and the maximum cooldown is always seven days).
- ``secondsPerBlock <uint256>``: An approximation of currently how many seconds are in between blocks.
- ``kitties <Kitty[]>``: An array containing the Kitty struct for all Kitties in existence. The ID of each cat is actually an index into this array. Note that ID 0 is a negacat, the unKitty, the mythical beast that is the parent of all gen0 cats. A bizarre creature that is both matron and sire... to itself! Has an invalid genetic code. In other words, cat ID 0 is invalid... ;-)
- ``kittyIndexToOwner <mapping (uint256 => address)>``: A mapping from cat IDs to the address that owns them. All cats have some valid owner address, even gen0 cats are created with a non-zero owner.
- ``ownershipTokenCount <mapping (address => uint256)>``: A mapping from owner address to count of tokens that address owns. Used internally inside balanceOf() to resolve ownership count.
- ``kittyIndexToApproved <mapping (uint256 => address)>``: A mapping from KittyIDs to an address that has been approved to call transferFrom(). Each Kitty can only have one approved address for transfer at any time. A zero value means no approval is outstanding.
- ``sireAllowedToAddress <mapping (uint256 => address)>``: A mapping from KittyIDs to an address that has been approved to use this Kitty for siring via breedWith(). Each Kitty can only have one approved address for siring at any time. A zero value means no approval is outstanding.
- ``saleAuction <SaleClockAuction>``: The address of the ClockAuction contract that handles sales of Kitties. This same contract handles both peer-to-peer sales as well as the gen0 sales which are initiated every 15 minutes.
- ``siringAuction <SiringClockAuction>``: The address of a custom ClockAuction subclassed contract that handles siring auctions. Needs to be separate from saleAuction because the actions taken on success after a sales and siring auction are quite different.

Events
------

Birth(address owner, uint256 kittyId, uint256 matronId, uint256 sireId, uint256 genes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Birth event is fired whenever a new kitten comes into existence. This obviously includes any time a cat is created through the giveBirth method, but it is also called when a new gen0 cat is created.

Parameters
""""""""""

- ``owner <address>``
- ``kittyId <uint256>``
- ``matronId <uint256>``
- ``sireId <uint256>``
- ``genes <uint256>``

Transfer(address from, address to, uint256 tokenId)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transfer event as defined in current draft of ERC721. Emitted every time a kitten ownership is assigned, including births.

Parameters
""""""""""

- ``from <address >``
- ``to <address >``
- ``tokenId <uint256 >``

External Functions
------------------


setSecondsPerBlock(uint256 secs) external onlyCLevel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Any C-level can fix how many seconds per blocks are currently observed.

Parameters
""""""""""

- ``secs <uint256>``

Returns
"""""""

None
