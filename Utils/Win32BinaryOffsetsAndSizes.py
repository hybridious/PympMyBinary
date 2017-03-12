class Win32BinaryOffsetsAndSizes:


    OFFSET_TO_PE_HEADER_OFFSET = 0x3C
    OFFSET_TO_ENTRYPOINT_RVA = 0x28
    OFFSET_TO_NUMBER_OF_SECTIONS = 0x6

    OFFSET_TO_SECTION_VIRTUAL_SIZE_WITHIN_SECTION_HEADER = 0X8
    OFFSET_TO_SECTION_RVA_WITHIN_SECTION_HEADER = 0XC
    OFFSET_TO_SECTION_RAW_SIZE_WITHIN_SECTION_HEADER = 0x10
    OFFSET_TO_SECTION_RAW_OFFSET_WITHIN_SECTION_HEADER = 0X14

    OFFSET_TO_SIZE_OF_CODE = 0x1C
    OFFSET_TO_BASE_OF_CODE_RVA = 0x2C
    OFFSET_TO_BASE_OF_DATA_RVA = 0x30
    OFFSET_TO_SECTION_ALIGNMENT = 0x38
    OFFSET_TO_FILE_ALIGNMENT = 0x3C
    OFFSET_TO_SIZE_OF_IMAGE = 0x50
    OFFSET_TO_CHECKSUM = 0x58
    CHECKSUM_SIZE = 0X4
    CHECKSUM_COMPUTATION_UNIT = 0x2 #Blocks of 16 bits

    SIZE_OF_DATA_DIRECTORY_HEADER_ENTRY = 0x8
    DATA_DIRECTORIES_HEADER_SIZE = 0x10

    OFFSET_TO_EXPORT_TABLE_RVA = 0X78
    OFFSET_TO_IMPORT_TABLE_RVA = 0x80
    OFFSET_TO_RESOURCE_TABLE_RVA = 0x88
    OFFSET_TO_EXCEPTION_TABLE_RVA = 0X90
    OFFSET_TO_CERTIFICATE_TABLE_RVA = 0x98
    OFFSET_TO_BASE_RELOCATION_TABLE_RVA = 0XA0
    OFFSET_TO_BASE_RELOCATION_TABLE_SIZE = 0xA4
    OFFSET_TO_DEBUG_RVA = 0XA8
    OFFSET_TO_ARCHITECTURE_DATA_RVA = 0XB0
    OFFSET_TO_GLOBAL_PTR_RVA = 0XB8
    OFFSET_TO_TLS_TABLE_RVA = 0XC0
    OFFSET_TO_LOAD_CONFIG_TABLE_RVA = 0XC8
    OFFSET_TO_BOUND_IMPORT_RVA = 0XD0
    OFFSET_TO_IMPORT_ADDRESS_TABLE_RVA = 0XD8
    OFFSET_TO_DELAY_IMPORT_DESCRIPTOR_RVA = 0XE0
    OFFSET_TO_CLR_RUNTIME_HEADER_RVA = 0XE8


    OFFSET_TO_BEGINNING_OF_SECTION_HEADERS = 0xF8

    SIZE_OF_SECTION_HEADER = 0x28

    #Resource headers
    OFFSET_TO_NUMBER_OF_ID_ENTRIES_WITHIN_RESOURCE_DIRECTORY_HEADER = 0xE
    OFFSET_TO_OFFSET_TO_DATA_ENTRY_WITHIN_LANGUAGE = 0x14

    #Import headers
    NUMBER_OF_DWORDS_WITHIN_EACH_DIRECTORY_TABLE_ENTRY = 0x5
    NUMBER_OF_BYTES_PER_IMPORT_DIRECTORY_TABLE_ENTRY = 0x14
    OFFSET_TO_IMPORT_NAME_TABLE_RVA_WITHIN_IMPORT_DIRECTORY_TABLE = 0x0
    OFFSET_TO_NAME_RVA_WITHIN_IMPORT_DIRECTORY_TABLE = 0xC
    OFFSET_TO_IMPORT_ADDRESS_TABLE_RVA_WITHIN_IMPORT_DIRECTORY_TABLE = 0x10

    #Export headers
    OFFSET_TO_NAME_RVA_WITHIN_EXPORT_DIRECTORY_TABLE = 0XC
    OFFSET_TO_NUMBER_OF_FUNCTIONS_WITHIN_EXPORT_DIRECTORY_TABLE = 0X14
    OFFSET_TO_NUMBER_OF_NAMES_WITHIN_EXPORT_DIRECTORY_TABLE = 0X18
    OFFSET_TO_ADDRESS_TABLE_RVA_WITHIN_EXPORT_DIRECTORY_TABLE = 0x1C
    OFFSET_TO_NAME_POINTER_TABLE_RVA_WITHIN_EXPORT_DIRECTORY_TABLE = 0X20
    OFFSET_TO_ORDINAL_TABLE_RVA_WITHIN_EXPORT_DIRECTORY_TABLE = 0X24