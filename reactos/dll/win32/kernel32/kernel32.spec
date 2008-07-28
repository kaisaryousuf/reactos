#
#   kernel32.spec
#
#   Exports for KERNEL32 DLL


@ stdcall AcquireSRWLockExclusive(ptr) ntdll.RtlAcquireSRWLockExclusive
@ stdcall AcquireSRWLockShare(ptr) ntdll.RtlAcquireSRWLockShared
@ stdcall ActivateActCtx(ptr ptr)
@ stdcall AddAtomA(str)
@ stdcall AddAtomW(wstr)
@ stdcall AddConsoleAliasA(str str str) #check
@ stdcall AddConsoleAliasW(wstr wstr wstr) #check
@ stub AddLocalAlternateComputerNameA
@ stub AddLocalAlternateComputerNameW
@ stdcall AddRefActCtx(ptr)
@ stdcall AddVectoredExceptionHandler(long ptr) ntdll.RtlAddVectoredExceptionHandler
@ stdcall AllocConsole()
@ stub AllocLSCallback
@ stub AllocateUserPhysicalPages
@ stdcall AreFileApisANSI()
@ stdcall AssignProcessToJobObject(ptr ptr)
@ stdcall AttachConsole(long)
@ stdcall BackupRead(ptr ptr long ptr long long ptr)
@ stdcall BackupSeek(ptr long long ptr ptr ptr)
@ stdcall BackupWrite(ptr ptr long ptr long long ptr)
@ stdcall BaseCheckAppcompatCache(long long long ptr) #check
@ stub BaseCleanupAppcompatCache
@ stub BaseCleanupAppcompatCacheSupport
@ stdcall BaseDumpAppcompatCache()
@ stdcall BaseFlushAppcompatCache()
@ stub BaseInitAppcompatCache
@ stub BaseInitAppcompatCacheSupport
@ stdcall BaseProcessInitPostImport()
@ stdcall BaseQueryModuleData(str str ptr ptr ptr) #check
@ stdcall BaseUpdateAppcompatCache(long long long)
@ stub BasepCheckWinSaferRestrictions
@ stub BasepDebugDump
@ stdcall Beep(long long)
@ stdcall BeginUpdateResourceA(str long)
@ stdcall BeginUpdateResourceW(wstr long)
@ stdcall BindIoCompletionCallback(long ptr long)
@ stdcall BuildCommDCBA(str ptr)
@ stdcall BuildCommDCBAndTimeoutsA(str ptr ptr)
@ stdcall BuildCommDCBAndTimeoutsW(wstr ptr ptr)
@ stdcall BuildCommDCBW(wstr ptr)
@ stdcall CallNamedPipeA(str ptr long ptr long ptr long)
@ stdcall CallNamedPipeW(wstr ptr long ptr long ptr long)
@ stdcall CancelDeviceWakeupRequest(long)
@ stdcall CancelIo(long)
@ stdcall CancelIoEx(long ptr)
@ stdcall CancelSynchronousIo(long)
@ stdcall CancelTimerQueueTimer(long long)
@ stdcall CancelWaitableTimer(long)
@ stdcall ChangeTimerQueueTimer(long long long long)
@ stdcall CheckNameLegalDOS8Dot3A(str str long long long)
@ stdcall CheckNameLegalDOS8Dot3W(wstr str long long long)
@ stdcall CheckRemoteDebuggerPresent(long ptr)
@ stdcall ClearCommBreak(long)
@ stdcall ClearCommError(long ptr ptr)
@ stdcall CloseConsoleHandle(long)
@ stdcall CloseHandle(long)
@ stdcall CloseProfileUserMapping()
@ stub CloseSystemHandle
@ stdcall CmdBatNotification(long)
@ stdcall CommConfigDialogA(str long ptr)
@ stdcall CommConfigDialogW(wstr long ptr)
@ stdcall CompareFileTime(ptr ptr)
@ stdcall CompareStringA(long long str long str long)
@ stdcall CompareStringW(long long wstr long wstr long)
@ stdcall ConnectNamedPipe(long ptr)
@ stdcall ConsoleMenuControl(long long long)
@ stub ConsoleSubst
@ stdcall ContinueDebugEvent(long long long)
@ stdcall ConvertDefaultLocale (long)
@ stdcall ConvertFiberToThread()
@ stdcall ConvertThreadToFiber(ptr)
@ stdcall ConvertThreadToFiberEx(ptr long)
@ stdcall CopyFileA(str str long)
@ stdcall CopyFileExA (str str ptr ptr ptr long)
@ stdcall CopyFileExW (wstr wstr ptr ptr ptr long)
@ stdcall CopyFileW(wstr wstr long)
@ stdcall CopyLZFile(long long) LZCopy
@ stdcall CreateActCtxA(ptr)
@ stdcall CreateActCtxW(ptr)
@ stdcall CreateConsoleScreenBuffer(long long ptr long ptr)
@ stdcall CreateDirectoryA(str ptr)
@ stdcall CreateDirectoryExA(str str ptr)
@ stdcall CreateDirectoryExW(wstr wstr ptr)
@ stdcall CreateDirectoryW(wstr ptr)
@ stdcall CreateEventA(ptr long long str)
@ stdcall CreateEventW(ptr long long wstr)
@ stdcall CreateFiber(long ptr ptr)
@ stdcall CreateFiberEx(long long long ptr ptr)
@ stdcall CreateFileA(str long long ptr long long long)
@ stdcall CreateFileMappingA(long ptr long long long str)
@ stdcall CreateFileMappingW(long ptr long long long wstr)
@ stdcall CreateFileW(wstr long long ptr long long long)
@ stdcall CreateHardLinkA(str str ptr)
@ stdcall CreateHardLinkW(wstr wstr ptr)
@ stdcall CreateIoCompletionPort(long long long long)
@ stdcall CreateJobObjectA(ptr str)
@ stdcall CreateJobObjectW(ptr wstr)
@ stdcall CreateJobSet(long ptr long)
@ stub CreateKernelThread
@ stdcall CreateMailslotA(ptr long long ptr)
@ stdcall CreateMailslotW(ptr long long ptr)
@ stdcall CreateMemoryResourceNotification(ptr)
@ stdcall CreateMutexA(ptr long str)
@ stdcall CreateMutexW(ptr long wstr)
@ stdcall CreateNamedPipeA(str long long long long long long ptr)
@ stdcall CreateNamedPipeW(wstr long long long long long long ptr)
@ stdcall CreateNlsSecurityDescriptor(ptr long long)
@ stdcall CreatePipe(ptr ptr ptr long)
@ stdcall CreateProcessA(str str ptr ptr long long ptr str ptr ptr)
@ stdcall CreateProcessInternalA(ptr str str ptr ptr long long ptr str ptr ptr long)
@ stdcall CreateProcessInternalW(ptr wstr wstr ptr ptr long long ptr wstr ptr ptr long)
@ stub CreateProcessInternalWSecure
@ stdcall CreateProcessW(wstr wstr ptr ptr long long ptr wstr ptr ptr)
@ stdcall CreateRemoteThread(long ptr long ptr long long ptr)
@ stdcall CreateSemaphoreA(ptr long long str)
@ stdcall CreateSemaphoreW(ptr long long wstr)
@ stdcall CreateSemaphoreExA(ptr long long str long long)
@ stdcall CreateSemaphoreExW(ptr long long wstr long long)
@ stdcall CreateSocketHandle()
@ stdcall CreateSymbolicLinkA(str str long)
@ stdcall CreateSymbolicLinkW(wstr wstr long)
@ stdcall CreateTapePartition(long long long long)
@ stdcall CreateThread(ptr long ptr long long ptr)
@ stdcall CreateTimerQueue ()
@ stdcall CreateTimerQueueTimer(ptr long ptr ptr long long long)
@ stdcall CreateToolhelp32Snapshot(long long)
@ stdcall CreateVirtualBuffer(long long long)
@ stdcall CreateWaitableTimerA(ptr long str)
@ stdcall CreateWaitableTimerW(ptr long wstr)
@ stdcall CreateWaitableTimerExA (ptr str long long)
@ stdcall CreateWaitableTimerExW (ptr wstr long long)
@ stdcall DeactivateActCtx(long ptr)
@ stdcall DebugActiveProcess(long)
@ stdcall DebugActiveProcessStop(long)
@ stdcall DebugBreak() ntdll.DbgBreakPoint
@ stdcall DebugBreakProcess(long)
@ stdcall DebugSetProcessKillOnExit(long)
@ stdcall DecodePointer(ptr) ntdll.RtlDecodePointer
@ stub DecodeSystemPointer
@ stdcall DefineDosDeviceA(long str str)
@ stdcall DefineDosDeviceW(long wstr wstr)
@ stdcall DelayLoadFailureHook(str str)
@ stdcall DeleteAtom(long)
@ stdcall DeleteCriticalSection(ptr) ntdll.RtlDeleteCriticalSection
@ stdcall DeleteFiber(ptr)
@ stdcall DeleteFileA(str)
@ stdcall DeleteFileW(wstr)
@ stdcall DeleteTimerQueue(long)
@ stdcall DeleteTimerQueueEx (long long)
@ stdcall DeleteTimerQueueTimer(long long long)
@ stdcall DeleteVolumeMountPointA(str) #check
@ stdcall DeleteVolumeMountPointW(wstr) #check
@ stdcall DeviceIoControl(long long ptr long ptr long ptr ptr)
@ stdcall DisableThreadLibraryCalls(long)
@ stdcall DisconnectNamedPipe(long)
@ stdcall DnsHostnameToComputerNameA (str ptr ptr)
@ stdcall DnsHostnameToComputerNameW (wstr ptr ptr)
@ stdcall DosDateTimeToFileTime(long long ptr)
@ stdcall DosPathToSessionPathA(long str str)
@ stdcall DosPathToSessionPathW(long wstr wstr)
@ stdcall DuplicateConsoleHandle(long long long long)
@ stdcall DuplicateHandle(long long long ptr long long long)
@ stdcall EncodePointer(ptr) ntdll.RtlEncodePointer
@ stub EncodeSystemPointer
@ stdcall EndUpdateResourceA(long long)
@ stdcall EndUpdateResourceW(long long)
@ stdcall EnterCriticalSection(ptr) ntdll.RtlEnterCriticalSection
@ stdcall EnumCalendarInfoA(ptr long long long)
@ stdcall EnumCalendarInfoExA(ptr long long long)
@ stdcall EnumCalendarInfoExW(ptr long long long)
@ stdcall EnumCalendarInfoW(ptr long long long)
@ stdcall EnumDateFormatsA(ptr long long)
@ stdcall EnumDateFormatsExA(ptr long long)
@ stdcall EnumDateFormatsExW(ptr long long)
@ stdcall EnumDateFormatsW(ptr long long)
@ stdcall EnumLanguageGroupLocalesA(ptr long long ptr)
@ stdcall EnumLanguageGroupLocalesW(ptr long long ptr)
@ stdcall EnumResourceLanguagesA(long str str ptr long)
@ stdcall EnumResourceLanguagesW(long wstr wstr ptr long)
@ stdcall EnumResourceNamesA(long str ptr long)
@ stdcall EnumResourceNamesW(long wstr ptr long)
@ stdcall EnumResourceTypesA(long ptr long)
@ stdcall EnumResourceTypesW(long ptr long)
@ stdcall EnumSystemCodePagesA(ptr long)
@ stdcall EnumSystemCodePagesW(ptr long)
@ stdcall EnumSystemGeoID(long long ptr)
@ stdcall EnumSystemLanguageGroupsA(ptr long ptr)
@ stdcall EnumSystemLanguageGroupsW(ptr long ptr)
@ stdcall EnumSystemLocalesA(ptr long)
@ stdcall EnumSystemLocalesW(ptr long)
@ stdcall EnumTimeFormatsA(ptr long long)
@ stdcall EnumTimeFormatsW(ptr long long)
@ stdcall EnumUILanguagesA(ptr long long)
@ stdcall EnumUILanguagesW(ptr long long)
@ stub EnumerateLocalComputerNamesA
@ stub EnumerateLocalComputerNamesW
@ stdcall EraseTape(ptr long long)
@ stdcall EscapeCommFunction(long long)
@ stdcall ExitProcess(long)
@ stdcall ExitThread(long)
@ stub ExitVDM
@ stdcall ExpandEnvironmentStringsA(str ptr long)
@ stdcall ExpandEnvironmentStringsW(wstr ptr long)
@ stdcall ExpungeConsoleCommandHistoryA(long)
@ stdcall ExpungeConsoleCommandHistoryW(long)
@ stdcall ExtendVirtualBuffer(long long)
@ stdcall FatalAppExitA(long str)
@ stdcall FatalAppExitW(long wstr)
@ stdcall FatalExit(long)
@ stdcall FileTimeToDosDateTime(ptr ptr ptr)
@ stdcall FileTimeToLocalFileTime(ptr ptr)
@ stdcall FileTimeToSystemTime(ptr ptr)
@ stdcall FillConsoleOutputAttribute(long long long long ptr)
@ stdcall FillConsoleOutputCharacterA(long long long long ptr)
@ stdcall FillConsoleOutputCharacterW(long long long long ptr)
@ stdcall FindActCtxSectionGuid(long ptr long ptr ptr)
@ stdcall FindActCtxSectionStringA(long ptr long str ptr)
@ stdcall FindActCtxSectionStringW(long ptr long wstr ptr)
@ stdcall FindAtomA(str)
@ stdcall FindAtomW(wstr)
@ stdcall FindClose(long)
@ stdcall FindCloseChangeNotification(long)
@ stdcall FindFirstChangeNotificationA(str long long)
@ stdcall FindFirstChangeNotificationW(wstr long long)
@ stdcall FindFirstFileA(str ptr)
@ stdcall FindFirstFileExA(str long ptr long ptr long)
@ stdcall FindFirstFileExW(wstr long ptr long ptr long)
@ stdcall FindFirstFileW(wstr ptr)
@ stdcall FindFirstStreamW(wstr ptr ptr long)
@ stdcall FindFirstVolumeA(ptr long)
@ stdcall FindFirstVolumeMountPointA(str ptr long)
@ stdcall FindFirstVolumeMountPointW(wstr ptr long)
@ stdcall FindFirstVolumeW(ptr long)
@ stdcall FindNextChangeNotification(long)
@ stdcall FindNextFileA(long ptr)
@ stdcall FindNextFileW(long ptr)
@ stdcall FindNextVolumeA(long ptr long)
@ stdcall FindNextVolumeMountPointA(long str long)
@ stdcall FindNextVolumeMountPointW(long wstr long)
@ stdcall FindNextVolumeW(long ptr long)
@ stdcall FindResourceA(long str str)
@ stdcall FindResourceExA(long str str long)
@ stdcall FindResourceExW(long wstr wstr long)
@ stdcall FindResourceW(long wstr wstr)
@ stdcall FindVolumeClose(ptr)
@ stdcall FindVolumeMountPointClose(ptr)
@ stdcall FlsAlloc(ptr)
@ stdcall FlsFree(long)
@ stdcall FlsGetValue(long)
@ stdcall FlsSetValue(long ptr)
@ stdcall FlushConsoleInputBuffer(long)
@ stdcall FlushFileBuffers(long)
@ stdcall FlushInstructionCache(long long long)
@ stdcall FlushViewOfFile(ptr long)
@ stdcall FoldStringA(long str long ptr long)
@ stdcall FoldStringW(long wstr long ptr long)
@ stdcall FormatMessageA(long ptr long long ptr long ptr)
@ stdcall FormatMessageW(long ptr long long ptr long ptr)
@ stdcall FreeConsole()
@ stdcall FreeEnvironmentStringsA(ptr)
@ stdcall FreeEnvironmentStringsW(ptr)
@ stdcall FreeLibrary(long)
@ stdcall FreeLibraryAndExitThread(long long)
@ stdcall FreeResource(long)
@ stdcall FreeUserPhysicalPages(long long long)
@ stdcall FreeVirtualBuffer(ptr)
@ stdcall GenerateConsoleCtrlEvent(long long)
@ stdcall GetACP()
@ stdcall GetAtomNameA(long ptr long)
@ stdcall GetAtomNameW(long ptr long)
@ stdcall GetBinaryType(str ptr) GetBinaryTypeA
@ stdcall GetBinaryTypeA(str ptr)
@ stdcall GetBinaryTypeW(wstr ptr)
@ stdcall GetCPFileNameFromRegistry(long wstr long) #check
@ stdcall GetCPInfo(long ptr)
@ stdcall GetCPInfoExA(long long ptr)
@ stdcall GetCPInfoExW(long long ptr)
@ stdcall GetCalendarInfoA(long long long ptr long ptr)
@ stdcall GetCalendarInfoW(long long long ptr long ptr)
@ stub GetComPlusPackageInstallStatus
@ stdcall GetCommConfig(long ptr long)
@ stdcall GetCommMask(long ptr)
@ stdcall GetCommModemStatus(long ptr)
@ stdcall GetCommProperties(long ptr)
@ stdcall GetCommState(long ptr)
@ stdcall GetCommTimeouts(long ptr)
@ stdcall GetCommandLineA()
@ stdcall GetCommandLineW()
@ stdcall GetCompressedFileSizeA(long ptr)
@ stdcall GetCompressedFileSizeW(long ptr)
@ stdcall GetComputerNameA(ptr ptr)
@ stdcall GetComputerNameExA(long ptr ptr)
@ stdcall GetComputerNameExW(long ptr ptr)
@ stdcall GetComputerNameW(ptr ptr)
@ stdcall GetConsoleAliasA(str str long str)
@ stdcall GetConsoleAliasExesA(str long)
@ stdcall GetConsoleAliasExesLengthA()
@ stdcall GetConsoleAliasExesLengthW()
@ stdcall GetConsoleAliasExesW(wstr long)
@ stdcall GetConsoleAliasW(wstr wstr long wstr)
@ stdcall GetConsoleAliasesA(str long str)
@ stdcall GetConsoleAliasesLengthA(str)
@ stdcall GetConsoleAliasesLengthW(wstr)
@ stdcall GetConsoleAliasesW(wstr long wstr)
@ stdcall GetConsoleCP()
@ stub GetConsoleCharType
@ stdcall GetConsoleCommandHistoryA(long long long) #check
@ stdcall GetConsoleCommandHistoryLengthA(long)#check
@ stdcall GetConsoleCommandHistoryLengthW(long)#check
@ stdcall GetConsoleCommandHistoryW(long long long)#check
@ stdcall GetConsoleCursorInfo(long ptr)
@ stub GetConsoleCursorMode
@ stdcall GetConsoleDisplayMode(ptr)
@ stub GetConsoleFontInfo
@ stub GetConsoleFontSize
@ stub GetConsoleHardwareState
@ stdcall GetConsoleInputExeNameA(long ptr)
@ stdcall GetConsoleInputExeNameW(long ptr)
@ stdcall GetConsoleInputWaitHandle()
@ stdcall GetConsoleKeyboardLayoutNameA(ptr)
@ stdcall GetConsoleKeyboardLayoutNameW(ptr)
@ stdcall GetConsoleMode(long ptr)
@ stub GetConsoleNlsMode
@ stdcall GetConsoleOutputCP()
@ stub GetConsoleProcessist
@ stdcall GetConsoleScreenBufferInfo(long ptr)
@ stub GetConsoleSelectionInfo
@ stdcall GetConsoleTitleA(ptr long)
@ stdcall GetConsoleTitleW(ptr long)
@ stdcall GetConsoleWindow()
@ stdcall GetCurrencyFormatA(long long str ptr str long)
@ stdcall GetCurrencyFormatW(long long str ptr str long)
@ stdcall GetCurrentActCtx(ptr)
@ stub GetCurrentConsoleFont
@ stdcall GetCurrentDirectoryA(long ptr)
@ stdcall GetCurrentDirectoryW(long ptr)
@ stdcall GetCurrentProcess()
@ stdcall GetCurrentProcessId()
@ stdcall GetCurrentThread()
@ stdcall GetCurrentThreadId()
@ stdcall GetDateFormatA(long long ptr str ptr long)
@ stdcall GetDateFormatW(long long ptr wstr ptr long)
@ stub GetDaylightFlag
@ stdcall GetDefaultCommConfigA(str ptr long)
@ stdcall GetDefaultCommConfigW(wstr ptr long)
@ stub GetDefaultSortkeySize
@ stdcall GetDevicePowerState(long ptr)
@ stdcall GetDiskFreeSpaceA(str ptr ptr ptr ptr)
@ stdcall GetDiskFreeSpaceExA (str ptr ptr ptr)
@ stdcall GetDiskFreeSpaceExW (wstr ptr ptr ptr)
@ stdcall GetDiskFreeSpaceW(wstr ptr ptr ptr ptr)
@ stdcall GetDllDirectoryA(long ptr)
@ stdcall GetDllDirectoryW(long ptr)
@ stdcall GetDriveTypeA(str)
@ stdcall GetDriveTypeW(wstr)
@ stdcall GetEnvironmentStrings()
@ stdcall GetEnvironmentStringsA() GetEnvironmentStrings
@ stdcall GetEnvironmentStringsW()
@ stdcall GetEnvironmentVariableA(str ptr long)
@ stdcall GetEnvironmentVariableW(wstr ptr long)
@ stub GetErrorMode
@ stdcall GetExitCodeProcess(long ptr)
@ stdcall GetExitCodeThread(long ptr)
@ stdcall GetExpandedNameA(str ptr)
@ stdcall GetExpandedNameW(wstr ptr)
@ stdcall GetFileAttributesA(str)
@ stdcall GetFileAttributesByHandle(long ptr long)
@ stdcall GetFileAttributesExA(str long ptr)
@ stdcall GetFileAttributesExW(wstr long ptr)
@ stdcall GetFileAttributesW(wstr)
@ stdcall GetFileBandwidthReservation(long ptr ptr ptr ptr ptr)
@ stdcall GetFileInformationByHandle(long ptr)
@ stdcall GetFileSize(long ptr)
@ stdcall GetFileSizeEx(long ptr)
@ stdcall GetFileTime(long ptr ptr ptr)
@ stdcall GetFileType(long)
@ stdcall GetFinalPathNameByHandleA(long str long long)
@ stdcall GetFinalPathNameByHandleW(long wstr long long)
@ stub GetFirmwareEnvironmentVariableA
@ stub GetFirmwareEnvironmentVariableW
@ stdcall GetFullPathNameA(str long ptr ptr)
@ stdcall GetFullPathNameW(wstr long ptr ptr)
@ stdcall GetGeoInfoA(long long ptr long long)
@ stdcall GetGeoInfoW(long long ptr long long)
@ stdcall GetHandleContext(long)
@ stdcall GetHandleInformation(long ptr)
@ stub GetSCallbackTarget
@ stub GetSCallbackTemplate
@ stdcall GetLargePageMinimum()
@ stdcall GetLargestConsoleWindowSize(long)
@ stdcall GetLastError()
@ stub GetLinguistLangSize
@ stdcall GetLocalTime(ptr)
@ stdcall GetLocaleInfoA(long long ptr long)
@ stdcall GetLocaleInfoW(long long ptr long)
@ stdcall GetLocaleInfoEx(wstr long wstr long)
@ stdcall GetLogicalDriveStringsA(long ptr)
@ stdcall GetLogicalDriveStringsW(long ptr)
@ stdcall GetLogicalDrives()
@ stdcall GetLongPathNameA (str long long)
@ stdcall GetLongPathNameW (wstr long long)
@ stdcall GetMailslotInfo(long ptr ptr ptr ptr)
@ stdcall GetModuleFileNameA(long ptr long)
@ stdcall GetModuleFileNameW(long ptr long)
@ stdcall GetModuleHandleA(str)
@ stdcall GetModuleHandleExA(long ptr ptr)
@ stdcall GetModuleHandleExW(long ptr ptr)
@ stdcall GetModuleHandleW(wstr)
@ stdcall GetNamedPipeHandleStateA(long ptr ptr ptr ptr str long)
@ stdcall GetNamedPipeHandleStateW(long ptr ptr ptr ptr wstr long)
@ stdcall GetNamedPipeInfo(long ptr ptr ptr ptr)
@ stdcall GetNativeSystemInfo(ptr)
@ stub GetNextVDMCommand
@ stub GetNlsSectionName
@ stub GetNumaAvailableMemory
@ stub GetNumaAvailableMemoryNode
@ stub GetNumaHighestNodeNumber
@ stub GetNumaNodeProcessorMask
@ stub GetNumaProcessorMap
@ stub GetNumaProcessorNode
@ stdcall GetNumberFormatA(long long str ptr ptr long)
@ stdcall GetNumberFormatW(long long wstr ptr ptr long)
@ stdcall GetNumberOfConsoleFonts()
@ stdcall GetNumberOfConsoleInputEvents(long ptr)
@ stdcall GetNumberOfConsoleMouseButtons(ptr)
@ stdcall GetOEMCP()
@ stdcall GetOverlappedResult(long ptr ptr long)
@ stdcall GetPriorityClass(long)
@ stdcall GetPrivateProfileIntA(str str long str)
@ stdcall GetPrivateProfileIntW(wstr wstr long wstr)
@ stdcall GetPrivateProfileSectionA(str ptr long str)
@ stdcall GetPrivateProfileSectionNamesA(ptr long str)
@ stdcall GetPrivateProfileSectionNamesW(ptr long wstr)
@ stdcall GetPrivateProfileSectionW(wstr ptr long wstr)
@ stdcall GetPrivateProfileStringA(str str str ptr long str)
@ stdcall GetPrivateProfileStringW(wstr wstr wstr ptr long wstr)
@ stdcall GetPrivateProfileStructA (str str ptr long str)
@ stdcall GetPrivateProfileStructW(wstr wstr ptr long wstr)
@ stdcall GetProcAddress(long str)
@ stdcall GetProcessAffinityMask(long ptr ptr)
@ stdcall GetProcessHandleCount(long ptr)
@ stdcall GetProcessHeap()
@ stdcall GetProcessHeaps(long ptr)
@ stdcall GetProcessId(long)
@ stdcall GetProcessIoCounters(long ptr)
@ stdcall GetProcessPriorityBoost(long ptr)
@ stdcall GetProcessShutdownParameters(ptr ptr)
@ stdcall GetProcessTimes(long ptr ptr ptr ptr)
@ stdcall GetProcessVersion(long)
@ stdcall GetProcessWorkingSetSize(long ptr ptr)
@ stub GetProductName
@ stdcall GetProfileIntA(str str long)
@ stdcall GetProfileIntW(wstr wstr long)
@ stdcall GetProfileSectionA(str ptr long)
@ stdcall GetProfileSectionW(wstr ptr long)
@ stdcall GetProfileStringA(str str str ptr long)
@ stdcall GetProfileStringW(wstr wstr wstr ptr long)
@ stdcall GetQueuedCompletionStatus(long ptr ptr ptr long)
@ stub GetLSCallbackTarget
@ stub GetLSCallbackTemplate
@ stdcall GetShortPathNameA(str ptr long)
@ stdcall GetShortPathNameW(wstr ptr long)
@ stdcall GetStartupInfoA(ptr)
@ stdcall GetStartupInfoW(ptr)
@ stdcall GetStdHandle(long)
@ stdcall GetStringTypeA(long long str long ptr)
@ stdcall GetStringTypeExA(long long str long ptr)
@ stdcall GetStringTypeExW(long long wstr long ptr)
@ stdcall GetStringTypeW(long wstr long ptr)
@ stdcall GetSystemDefaultLCID()
@ stdcall GetSystemDefaultLangID()
@ stdcall GetSystemDefaultUILanguage()
@ stdcall GetSystemDirectoryA(ptr long)
@ stdcall GetSystemDirectoryW(ptr long)
@ stdcall GetSystemInfo(ptr)
@ stdcall GetSystemPowerStatus(ptr)
@ stub GetSystemRegistryQuota
@ stdcall GetSystemTime(ptr)
@ stdcall GetSystemTimeAdjustment(ptr ptr ptr)
@ stdcall GetSystemTimeAsFileTime(ptr)
@ stub GetSystemTimes
@ stdcall GetSystemWindowsDirectoryA(ptr long)
@ stdcall GetSystemWindowsDirectoryW(ptr long)
@ stdcall GetSystemWow64DirectoryA(ptr long)
@ stdcall GetSystemWow64DirectoryW(ptr long)
@ stdcall GetTapeParameters(ptr long ptr ptr)
@ stdcall GetTapePosition(ptr long ptr ptr ptr)
@ stdcall GetTapeStatus(ptr)
@ stdcall GetTempFileNameA(str str long ptr)
@ stdcall GetTempFileNameW(wstr wstr long ptr)
@ stdcall GetTempPathA(long ptr)
@ stdcall GetTempPathW(long ptr)
@ stdcall GetThreadContext(long ptr)
@ stdcall GetThreadId(ptr)
@ stub GetThreadIOPendingFlag
@ stdcall GetThreadLocale()
@ stdcall GetThreadPriority(long)
@ stdcall GetThreadPriorityBoost(long ptr)
@ stdcall GetThreadSelectorEntry(long long ptr)
@ stdcall GetThreadTimes(long ptr ptr ptr ptr)
@ stdcall GetTickCount()
@ stdcall -ret64 GetTickCount64()
@ stdcall GetTimeFormatA(long long ptr str ptr long)
@ stdcall GetTimeFormatW(long long ptr wstr ptr long)
@ stdcall GetTimeZoneInformation(ptr)
@ stdcall GetUserDefaultLCID()
@ stdcall GetUserDefaultLangID()
@ stdcall GetUserDefaultUILanguage()
@ stdcall GetUserGeoID(long)
@ stub GetVDMCurrentDirectories
@ stdcall GetVersion()
@ stdcall GetVersionExA(ptr)
@ stdcall GetVersionExW(ptr)
@ stdcall GetVolumeInformationA(str ptr long ptr ptr ptr ptr long)
@ stdcall GetVolumeInformationW(wstr ptr long ptr ptr ptr ptr long)
@ stdcall GetVolumeNameForVolumeMountPointA(str ptr long)
@ stdcall GetVolumeNameForVolumeMountPointW(wstr ptr long)
@ stdcall GetVolumePathNameA(str ptr long)
@ stdcall GetVolumePathNameW(wstr ptr long)
@ stub GetVolumePathNamesForVolumeNameA
@ stub GetVolumePathNamesForVolumeNameW
@ stdcall GetWindowsDirectoryA(ptr long)
@ stdcall GetWindowsDirectoryW(ptr long)
@ stub GetWriteWatch
@ stdcall GlobalAddAtomA(str)
@ stdcall GlobalAddAtomW(wstr)
@ stdcall GlobalAlloc(long long)
@ stdcall GlobalCompact(long)
@ stdcall GlobalDeleteAtom(long)
@ stdcall GlobalFindAtomA(str)
@ stdcall GlobalFindAtomW(wstr)
@ stdcall GlobalFix(long)
@ stdcall GlobalFlags(long)
@ stdcall GlobalFree(long)
@ stdcall GlobalGetAtomNameA(long ptr long)
@ stdcall GlobalGetAtomNameW(long ptr long)
@ stdcall GlobalHandle(ptr)
@ stdcall GlobalLock(long)
@ stdcall GlobalMemoryStatus(ptr)
@ stdcall GlobalMemoryStatusEx(ptr)
@ stdcall GlobalReAlloc(long long long)
@ stdcall GlobalSize(long)
@ stdcall GlobalUnWire(long)
@ stdcall GlobalUnfix(long)
@ stdcall GlobalUnlock(long)
@ stdcall GlobalWire(long)
@ stub Heap32First
@ stdcall Heap32ListFirst(long ptr)
@ stub Heap32ListNext
@ stub Heap32Next
@ stdcall HeapAlloc(long long long) ntdll.RtlAllocateHeap
@ stdcall HeapCompact(long long)
@ stdcall HeapCreate(long long long)
@ stub HeapCreateTagsW
@ stdcall HeapDestroy(long)
@ stub HeapExtend
@ stdcall HeapFree(long long long) ntdll.RtlFreeHeap
@ stdcall HeapLock(long)
@ stub HeapQueryInformation
@ stub HeapQueryTagW
@ stdcall HeapReAlloc(long long ptr long) ntdll.RtlReAllocateHeap
@ stub HeapSetFlags
@ stdcall HeapSetInformation(ptr long ptr long)
@ stdcall HeapSize(long long ptr) ntdll.RtlSizeHeap
@ stub HeapSummary
@ stdcall HeapUnlock(long)
@ stub HeapUsage
@ stdcall HeapValidate(long long ptr)
@ stdcall HeapWalk(long ptr)
@ stdcall InitAtomTable(long)
@ stdcall InitializeCriticalSection(ptr)
@ stdcall InitializeCriticalSectionAndSpinCount(ptr long)
#@ stdcall InitializeCriticalSectionEx(ptr long long)
@ stdcall InitializeSListHead(ptr) ntdll.RtlInitializeSListHead
@ stdcall InitializeSRWLock(ptr) ntdll.RtlInitializeSRWLock
@ stdcall InterlockedCompareExchange (ptr long long)
@ stdcall InterlockedDecrement(ptr)
@ stdcall InterlockedExchange(ptr long)
@ stdcall InterlockedExchangeAdd (ptr long )
@ stdcall InterlockedFlushSList(ptr) ntdll.RtlInterlockedFlushSList
@ stdcall InterlockedIncrement(ptr)
@ stdcall InterlockedPopEntrySList(ptr) ntdll.RtlInterlockedPopEntrySList
@ stdcall InterlockedPushEntrySList(ptr ptr) ntdll.RtlInterlockedPushEntrySList
@ stub InvalidateConsoleDIBits
@ stub InvalidateNSCache
@ stdcall IsBadCodePtr(ptr)
@ stdcall IsBadHugeReadPtr(ptr long)
@ stdcall IsBadHugeWritePtr(ptr long)
@ stdcall IsBadReadPtr(ptr long)
@ stdcall IsBadStringPtrA(ptr long)
@ stdcall IsBadStringPtrW(ptr long)
@ stdcall IsBadWritePtr(ptr long)
@ stdcall IsDBCSLeadByte(long)
@ stdcall IsDBCSLeadByteEx(long long)
@ stdcall IsDebuggerPresent()
@ stub IsProcessInJob
@ stdcall IsProcessorFeaturePresent(long)
@ stdcall IsSystemResumeAutomatic()
@ stdcall IsValidCodePage(long)
@ stdcall IsValidLanguageGroup(long long)
@ stdcall IsValidLocale(long long)
@ stub IsValidUILanguage
@ stdcall IsWow64Process(ptr ptr)
@ stub LCIDToLocaleName
@ stdcall LCMapStringA(long long str long ptr long)
@ stdcall LCMapStringW(long long wstr long ptr long)
@ stdcall LeaveCriticalSection(ptr) ntdll.RtlLeaveCriticalSection
@ stdcall LoadLibraryA(str)
@ stdcall LoadLibraryExA( str long long)
@ stdcall LoadLibraryExW(wstr long long)
@ stdcall LoadLibraryW(wstr)
@ stdcall LoadModule(str ptr)
@ stdcall LoadResource(long long)
@ stdcall LocalAlloc(long long)
@ stdcall LocalCompact(long)
@ stdcall LocalFileTimeToFileTime(ptr ptr)
@ stdcall LocalFlags(long)
@ stdcall LocalFree(long)
@ stdcall LocalHandle(ptr)
@ stdcall LocalLock(long)
@ stdcall LocalReAlloc(long long long)
@ stdcall LocalShrink(long long)
@ stdcall LocalSize(long)
@ stdcall LocalUnlock(long)
@ stub LocaleNameToLCID
@ stdcall LockFile(long long long long long)
@ stdcall LockFileEx(long long long long long ptr)
@ stdcall LockResource(long)
@ stdcall LZClose(long)
@ stdcall LZCopy(long long)
@ stdcall LZDone()
@ stdcall LZInit(long)
@ stdcall LZOpenFileA(str ptr long)
@ stdcall LZOpenFileW(wstr ptr long)
@ stdcall LZRead(long str long) #check
@ stdcall LZSeek(long long long) #check
@ stdcall LZStart()
@ stdcall MapUserPhysicalPages(ptr long ptr)
@ stdcall MapUserPhysicalPagesScatter(ptr long ptr)
@ stdcall MapViewOfFile(long long long long long)
@ stdcall MapViewOfFileEx(long long long long long ptr)
@ stdcall Module32First(long ptr)
@ stdcall Module32FirstW(long ptr)
@ stdcall Module32Next(long ptr)
@ stdcall Module32NextW(long ptr)
@ stdcall MoveFileA(str str)
@ stdcall MoveFileExA(str str long)
@ stdcall MoveFileExW(wstr wstr long)
@ stdcall MoveFileW(wstr wstr)
@ stdcall MoveFileWithProgressA(str str ptr ptr long)
@ stdcall MoveFileWithProgressW(wstr wstr ptr ptr long)
@ stdcall MulDiv(long long long)
@ stdcall MultiByteToWideChar(long long str long ptr long)
@ stdcall NeedCurrentDirectoryForExePathA(str)
@ stdcall NeedCurrentDirectoryForExePathW(wstr)
@ stub NlsConvertIntegerToString
@ stub NlsGetCacheUpdateCount
@ stub NlsResetProcessocale
@ stub NotifyNLSUserCache
@ stub NumaVirtualQueryNode
@ stdcall OpenConsoleW(wstr long long long)
@ stub OpenDataFile
@ stdcall OpenEventA(long long str)
@ stdcall OpenEventW(long long wstr)
@ stdcall OpenFile(str ptr long)
@ stdcall OpenFileMappingA(long long str)
@ stdcall OpenFileMappingW(long long wstr)
@ stub OpenJobObjectA
@ stub OpenJobObjectW
@ stdcall OpenMutexA(long long str)
@ stdcall OpenMutexW(long long wstr)
@ stdcall OpenProcess(long long long)
@ stub OpenProfileUserMapping
@ stdcall OpenSemaphoreA(long long str)
@ stdcall OpenSemaphoreW(long long wstr)
@ stdcall OpenThread(long long long)
@ stdcall OpenWaitableTimerA(long long str)
@ stdcall OpenWaitableTimerW(long long wstr)
@ stdcall OutputDebugStringA(str)
@ stdcall OutputDebugStringW(wstr)
@ stdcall PeekConsoleInputA(ptr ptr long ptr)
@ stdcall PeekConsoleInputW(ptr ptr long ptr)
@ stdcall PeekNamedPipe(long ptr long ptr ptr ptr)
@ stdcall PostQueuedCompletionStatus(long long ptr ptr)
@ stdcall PrepareTape(ptr long long)
@ stub PrivCopyFileExW
@ stub PrivMoveFileIdentityW
@ stdcall Process32First (ptr ptr)
@ stdcall Process32FirstW (ptr ptr)
@ stdcall Process32Next (ptr ptr)
@ stdcall Process32NextW (ptr ptr)
@ stdcall ProcessIdToSessionId(long ptr)
@ stdcall PulseEvent(long)
@ stdcall PurgeComm(long long)
@ stdcall QueryActCtxW(long ptr ptr long ptr long ptr)
@ stdcall QueryDepthSList(ptr) ntdll.RtlQueryDepthSList
@ stdcall QueryDosDeviceA(str ptr long)
@ stdcall QueryDosDeviceW(wstr ptr long)
@ stub QueryInformationJobObject
@ stub QueryMemoryResourceNotification
@ stub QueryNumberOfEventogRecords
@ stub QueryOldestEventogRecord
@ stdcall QueryPerformanceCounter(ptr)
@ stdcall QueryPerformanceFrequency(ptr)
@ stub QueryWin31IniFilesMappedToRegistry
@ stdcall QueueUserAPC(ptr long long)
@ stdcall QueueUserWorkItem(ptr ptr long)
@ stdcall RaiseException(long long long ptr)
@ stdcall ReadConsoleA(long ptr long ptr ptr)
@ stdcall ReadConsoleInputA(long ptr long ptr)
@ stub ReadConsoleInputExA
@ stub ReadConsoleInputExW
@ stdcall ReadConsoleInputW(long ptr long ptr)
@ stdcall ReadConsoleOutputA(long ptr long long ptr)
@ stdcall ReadConsoleOutputAttribute(long ptr long long ptr)
@ stdcall ReadConsoleOutputCharacterA(long ptr long long ptr)
@ stdcall ReadConsoleOutputCharacterW(long ptr long long ptr)
@ stdcall ReadConsoleOutputW(long ptr long long ptr)
@ stdcall ReadConsoleW(long ptr long ptr ptr)
@ stdcall ReadDirectoryChangesW(long ptr long long long ptr ptr ptr)
@ stdcall ReadFile(long ptr long ptr ptr)
@ stdcall ReadFileEx(long ptr long ptr ptr)
@ stdcall ReadFileScatter(long ptr long ptr ptr)
@ stdcall ReadProcessMemory(long ptr ptr long ptr)
@ stdcall RegisterApplicationRestart(wstr long)
@ stub RegisterConsoleIME
@ stub RegisterConsoleOS2
@ stub RegisterConsoleVDM
@ stub RegisterServiceProcess
@ stub RegisterSysMsgHandler
@ stub RegisterWaitForInputIdle
@ stdcall RegisterWaitForSingleObject(ptr long ptr ptr long long)
@ stdcall RegisterWaitForSingleObjectEx(long ptr ptr long long)
@ stub RegisterWowBaseHandlers
@ stub RegisterWowExec
@ stdcall ReleaseActCtx(ptr)
@ stdcall ReleaseMutex(long)
@ stdcall ReleaseSemaphore(long long ptr)
@ stdcall ReleaseSRWLockExclusive(ptr) ntdll.RtlReleaseSRWLockExclusive
@ stdcall ReleaseSRWLockShared(ptr) ntdll.RtlReleaseSRWLockShared
@ stdcall RemoveDirectoryA(str)
@ stdcall RemoveDirectoryW(wstr)
@ stub RemoveLocalAlternateComputerNameA
@ stub RemoveLocalAlternateComputerNameW
@ stdcall RemoveVectoredExceptionHandler(ptr) ntdll.RtlRemoveVectoredExceptionHandler
@ stdcall ReplaceFile(wstr wstr wstr long ptr ptr) ReplaceFileW
@ stdcall ReplaceFileA(str str str long ptr ptr)
@ stdcall ReplaceFileW(wstr wstr wstr long ptr ptr)
@ stub RequestDeviceWakeup
@ stdcall RequestWakeupLatency(long)
@ stdcall ResetEvent(long)
@ stub ResetWriteWatch
@ stdcall RestoreLastError(long) ntdll.RtlRestoreLastWin32Error
@ stdcall ResumeThread(long)
@ stdcall RtlCaptureContext(ptr) ntdll.RtlCaptureContext
@ stdcall RtlCaptureStackBackTrace(long long ptr ptr)  ntdll.RtlCaptureStackBackTrace
@ stdcall RtlFillMemory(ptr long long) ntdll.RtlFillMemory
@ stdcall RtlMoveMemory(ptr ptr long) ntdll.RtlMoveMemory
@ stdcall RtlUnwind(ptr ptr ptr long) ntdll.RtlUnwind
@ stdcall RtlZeroMemory(ptr long) ntdll.RtlZeroMemory
@ stdcall ScrollConsoleScreenBufferA(long ptr ptr ptr ptr)
@ stdcall ScrollConsoleScreenBufferW(long ptr ptr ptr ptr)
@ stdcall SearchPathA(str str str long ptr ptr)
@ stdcall SearchPathW(wstr wstr wstr long ptr ptr)
@ stdcall SetCPGlobal(long)
@ stdcall SetCalendarInfoA(long long long str)
@ stdcall SetCalendarInfoW(long long long wstr)
@ stub SetClientTimeZoneInformation
@ stub SetComPlusPackageInstallStatus
@ stdcall SetCommBreak(long)
@ stdcall SetCommConfig(long ptr long)
@ stdcall SetCommMask(long ptr)
@ stdcall SetCommState(long ptr)
@ stdcall SetCommTimeouts(long ptr)
@ stdcall SetComputerNameA(str)
@ stdcall SetComputerNameExA(long str)
@ stdcall SetComputerNameExW(long wstr)
@ stdcall SetComputerNameW(wstr)
@ stdcall SetConsoleActiveScreenBuffer(long)
@ stdcall SetConsoleCP(long)
@ stub SetConsoleCommandHistoryMode
@ stdcall SetConsoleCtrlHandler(ptr long)
@ stub SetConsoleCursor
@ stdcall SetConsoleCursorInfo(long ptr)
@ stub SetConsoleCursorMode
@ stdcall SetConsoleCursorPosition(long long)
@ stdcall SetConsoleDisplayMode(long long ptr)
@ stub SetConsoleFont
@ stub SetConsoleHardwareState
@ stub SetConsoleIcon
@ stdcall SetConsoleInputExeNameA(ptr)
@ stdcall SetConsoleInputExeNameW(ptr)
@ stub SetConsoleKeyShortcuts
@ stub SetConsoleLocalEUDC
@ stub SetConsoleMaximumWindowSize
@ stub SetConsoleMenuClose
@ stdcall SetConsoleMode(long long)
@ stub SetConsoleNlsMode
@ stub SetConsoleNumberOfCommandsA
@ stub SetConsoleNumberOfCommandsW
@ stub SetConsoleOS2OemFormat
@ stdcall SetConsoleOutputCP(long)
@ stub SetConsolePalette
@ stdcall SetConsoleScreenBufferSize(long long)
@ stdcall SetConsoleTextAttribute(long long)
@ stdcall SetConsoleTitleA(str)
@ stdcall SetConsoleTitleW(wstr)
@ stdcall SetConsoleWindowInfo(long long ptr)
@ stdcall SetCriticalSectionSpinCount(ptr long) ntdll.RtlSetCriticalSectionSpinCount
@ stdcall SetCurrentDirectoryA(str)
@ stdcall SetCurrentDirectoryW(wstr)
@ stub SetDaylightFlag
@ stdcall SetDefaultCommConfigA(str ptr long)
@ stdcall SetDefaultCommConfigW(wstr ptr long)
@ stdcall SetDllDirectoryA(str)
@ stdcall SetDllDirectoryW(wstr)
@ stdcall SetEndOfFile(long)
@ stdcall SetEnvironmentVariableA(str str)
@ stdcall SetEnvironmentVariableW(wstr wstr)
@ stdcall SetErrorMode(long)
@ stdcall SetEvent(long)
@ stdcall SetFileApisToANSI()
@ stdcall SetFileApisToOEM()
@ stdcall SetFileAttributesA(str long)
@ stdcall SetFileAttributesW(wstr long)
@ stdcall SetFilePointer(long long ptr long)
@ stdcall SetFilePointerEx(long double ptr long)
@ stub SetFileShortNameA
@ stub SetFileShortNameW
@ stdcall SetFileTime(long ptr ptr ptr)
@ stub SetFileValidData
@ stub SetFirmwareEnvironmentVariableA
@ stub SetFirmwareEnvironmentVariableW
@ stdcall SetHandleContext(long long)
@ stdcall SetHandleCount(long)
@ stdcall SetHandleInformation(long long long)
@ stub SetInformationJobObject
@ stub SetastConsoleEventActive
@ stdcall SetLastError(long)
@ stub SetocalPrimaryComputerNameA
@ stub SetocalPrimaryComputerNameW
@ stdcall SetLocalTime(ptr)
@ stdcall SetLocaleInfoA(long long str)
@ stdcall SetLocaleInfoW(long long wstr)
@ stdcall SetMailslotInfo(long long)
@ stub SetMessageWaitingIndicator
@ stdcall SetNamedPipeHandleState(long ptr ptr ptr)
@ stdcall SetPriorityClass(long long)
@ stdcall SetProcessAffinityMask(long long)
@ stdcall SetProcessPriorityBoost(long long)
@ stdcall SetProcessShutdownParameters(long long)
@ stdcall SetProcessWorkingSetSize(long long long)
@ stdcall SetStdHandle(long long)
@ stdcall SetSystemPowerState(long long)
@ stdcall SetSystemTime(ptr)
@ stdcall SetSystemTimeAdjustment(long long)
@ stdcall SetTapeParameters(ptr long ptr)
@ stdcall SetTapePosition(ptr long long long long long)
@ stdcall SetTermsrvAppInstallMode(long)
@ stdcall SetThreadAffinityMask(long long)
@ stdcall SetThreadContext(long ptr)
@ stdcall SetThreadExecutionState(long)
@ stdcall SetThreadIdealProcessor(long long)
@ stdcall SetThreadLocale(long)
@ stdcall SetThreadPriority(long long)
@ stdcall SetThreadPriorityBoost(long long)
@ stdcall SetThreadUILanguage(long)
@ stdcall SetTimeZoneInformation(ptr)
@ stub SetTimerQueueTimer
@ stdcall SetUnhandledExceptionFilter(ptr)
@ stdcall SetUserGeoID(long)
@ stub SetVDMCurrentDirectories
@ stdcall SetVolumeLabelA(str str)
@ stdcall SetVolumeLabelW(wstr wstr)
@ stub SetVolumeMountPointA
@ stub SetVolumeMountPointW
@ stdcall SetWaitableTimer(long ptr long ptr ptr long)
@ stdcall SetupComm(long long long)
@ stub ShowConsoleCursor
@ stdcall SignalObjectAndWait(long long long long)
@ stdcall SizeofResource(long long)
@ stdcall Sleep(long)
@ stdcall SleepEx(long long)
@ stdcall SuspendThread(long)
@ stdcall SwitchToFiber(ptr)
@ stdcall SwitchToThread()
@ stdcall SystemTimeToFileTime(ptr ptr)
@ stdcall SystemTimeToTzSpecificLocalTime (ptr ptr ptr)
@ stub TerminateJobObject
@ stdcall TerminateProcess(long long)
@ stdcall TerminateThread(long long)
@ stdcall TermsrvAppInstallMode()
@ stdcall Thread32First(long ptr)
@ stdcall Thread32Next(long ptr)
@ stdcall TlsAlloc()
@ stub TlsAllocInternal
@ stdcall TlsFree(long)
@ stub TlsFreeInternal
@ stdcall TlsGetValue(long)
@ stdcall TlsSetValue(long ptr)
@ stdcall Toolhelp32ReadProcessMemory(long ptr ptr long ptr)
@ stdcall TransactNamedPipe(long ptr long ptr long ptr ptr)
@ stdcall TransmitCommChar(long long)
@ stdcall TrimVirtualBuffer(ptr)
@ stdcall TryEnterCriticalSection(ptr) ntdll.RtlTryEnterCriticalSection
@ stdcall TzSpecificLocalTimeToSystemTime(ptr ptr ptr)
@ stdcall UTRegister(long str str str ptr ptr ptr)
@ stdcall UTUnRegister(long)
@ stdcall UnhandledExceptionFilter(ptr)
@ stdcall UnlockFile(long long long long long)
@ stdcall UnlockFileEx(long long long long ptr)
@ stdcall UnmapViewOfFile(ptr)
@ stub UnregisterConsoleIME
@ stdcall UnregisterWait(long)
@ stdcall UnregisterWaitEx(long long)
@ stdcall UpdateResourceA(long str str long ptr long)
@ stdcall UpdateResourceW(long wstr wstr long ptr long)
@ stub VDMConsoleOperation
@ stub VDMOperationStarted
@ stub ValidateCType
@ stub ValidatLeocale
@ stdcall VerLanguageNameA(long str long)
@ stdcall VerLanguageNameW(long wstr long)
@ stdcall -ret64 VerSetConditionMask(long long long long) ntdll.VerSetConditionMask
@ stdcall VerifyConsoleIoHandle(long)
@ stdcall VerifyVersionInfoA(long long double)
@ stdcall VerifyVersionInfoW(long long double)
@ stdcall VirtualAlloc(ptr long long long)
@ stdcall VirtualAllocEx(long ptr long long long)
@ stub VirtualBufferExceptionHandler
@ stdcall VirtualFree(ptr long long)
@ stdcall VirtualFreeEx(long ptr long long)
@ stdcall VirtualLock(ptr long)
@ stdcall VirtualProtect(ptr long long ptr)
@ stdcall VirtualProtectEx(long ptr long long ptr)
@ stdcall VirtualQuery(ptr ptr long)
@ stdcall VirtualQueryEx(long ptr ptr long)
@ stdcall VirtualUnlock(ptr long)
@ stdcall WakeAllConditionVariable(ptr) ntdll.RtlWakeAllConditionVariable
@ stdcall WakeConditionVariable(ptr) ntdll.RtlWakeConditionVariable
@ stdcall WaitCommEvent(long ptr ptr)
@ stdcall WaitForDebugEvent(ptr long)
@ stdcall WaitForMultipleObjects(long ptr long long)
@ stdcall WaitForMultipleObjectsEx(long ptr long long long)
@ stdcall WaitForSingleObject(long long)
@ stdcall WaitForSingleObjectEx(long long long)
@ stdcall WaitNamedPipeA (str long)
@ stdcall WaitNamedPipeW (wstr long)
@ stdcall WideCharToMultiByte(long long wstr long ptr long ptr ptr)
@ stdcall WinExec(str long)
@ stdcall Wow64EnableWow64FsRedirection(long)
@ stdcall Wow64DisableWow64FsRedirection(long)
@ stdcall Wow64RevertWow64FsRedirection(long)
@ stdcall WriteConsoleA(long ptr long ptr ptr)
@ stdcall WriteConsoleInputA(long ptr long ptr)
@ stub WriteConsoleInputVDMA
@ stub WriteConsoleInputVDMW
@ stdcall WriteConsoleInputW(long ptr long ptr)
@ stdcall WriteConsoleOutputA(long ptr long long ptr)
@ stdcall WriteConsoleOutputAttribute(long ptr long long ptr)
@ stdcall WriteConsoleOutputCharacterA(long ptr long long ptr)
@ stdcall WriteConsoleOutputCharacterW(long ptr long long ptr)
@ stdcall WriteConsoleOutputW(long ptr long long ptr)
@ stdcall WriteConsoleW(long ptr long ptr ptr)
@ stdcall WriteFile(long ptr long ptr ptr)
@ stdcall WriteFileEx(long ptr long ptr ptr)
@ stdcall WriteFileGather(long ptr long ptr ptr)
@ stdcall WritePrivateProfileSectionA(str str str)
@ stdcall WritePrivateProfileSectionW(wstr wstr wstr)
@ stdcall WritePrivateProfileStringA(str str str str)
@ stdcall WritePrivateProfileStringW(wstr wstr wstr wstr)
@ stdcall WritePrivateProfileStructA (str str ptr long str)
@ stdcall WritePrivateProfileStructW(wstr wstr ptr long wstr)
@ stdcall WriteProcessMemory(long ptr ptr long ptr)
@ stdcall WriteProfileSectionA(str str)
@ stdcall WriteProfileSectionW(str str)
@ stdcall WriteProfileStringA(str str str)
@ stdcall WriteProfileStringW(wstr wstr wstr)
@ stdcall WriteTapemark(ptr long long long)
@ stdcall WTSGetActiveConsoleSessionId()
@ stdcall ZombifyActCtx(ptr)
@ stub _DebugOut
@ stub _DebugPrintf
@ stdcall _hread(long ptr long)
@ stdcall _hwrite(long ptr long)
@ stdcall _lclose(long)
@ stdcall _lcreat(str long)
@ stdcall _llseek(long long long)
@ stdcall _lopen(str long)
@ stdcall _lread(long ptr long) _hread
@ stdcall _lwrite(long ptr long) _hwrite
@ stub dprintf
@ stdcall lstrcat(str str) lstrcatA
@ stdcall lstrcatA(str str)
@ stdcall lstrcatW(wstr wstr)
@ stdcall lstrcmp(str str) lstrcmpA
@ stdcall lstrcmpA(str str)
@ stdcall lstrcmpW(wstr wstr)
@ stdcall lstrcmpi(str str) lstrcmpiA
@ stdcall lstrcmpiA(str str)
@ stdcall lstrcmpiW(wstr wstr)
@ stdcall lstrcpy(ptr str) lstrcpyA
@ stdcall lstrcpyA(ptr str)
@ stdcall lstrcpyW(ptr wstr)
@ stdcall lstrcpyn(ptr str long) lstrcpynA
@ stdcall lstrcpynA(ptr str long)
@ stdcall lstrcpynW(ptr wstr long)
@ stdcall lstrlen(str) lstrlenA
@ stdcall lstrlenA(str)
@ stdcall lstrlenW(wstr)

#EOF
