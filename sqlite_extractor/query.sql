-- Messages
--
--	EventID 
--	Type 
--	Status
--	Subject
--	Body
--	Flag
--	PayloadPath
--	ThumbnailPath
--	StickerID
--	PttID
--	PttStatus
--	Duration
--	PGMessageId
--	PGIsLiked
--	PGLikeCount
----------------------------------------------------------

-- Events
--
-- 	EventID 
--	TimeStamp
--	Direction
--	Type
--	ContactLongitude
--	ContactLatitude
--	ChatID
--	Number
--	IsSessionLifeTime
--	Flags
--	Token
--	IsRead
-----------------------------------------------------------

-- EventsInfo
--
--	EventID
--	TimeStamp
--	Direction
--	EventType
--	EventToken
--	IsRead
--	ContactLongitude
--	ContactLatitude
--	ChatID
--	ChatToken
--	MessageType
--	MessageStatus
--	Subject
--	Body
--	Flag
--	PayloadPath
--	ThumbnailPath
--	StickerID
--	PttID
--	PttStatus
--	Duration
--	CallType
--	CallStatus
--	Number
--	EventFlags
--	ChatFlags
--	PGMessageId
--	PGIsLiked
--	PGLikeCount

-------------------------------------------------------------
-- Calls             Contact           EventsMetaData    UploadFile      
-- ChatCache         ContactRelation   Messages          Versions        
-- ChatInfo          DownloadFile      OriginNumberInfo
-- ChatRecovery      EventInfo         PhoneNumber     
-- ChatRelation      Events            Settings        


SELECT
	EventInfo.TimeStamp,
	EventInfo.Direction,
	EventInfo.Number,
	EventInfo.Body
FROM EventInfo 
WHERE EventInfo.Number = '+375447233234';