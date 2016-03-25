try:
    import lldb
    import datetime
except:
    pass


def log(d):
    """
    Log results
    """
    with open("{0}-xpc-log".format(datetime.date.today()), "a+") as f:
        f.writelines("%s" % d)
        f.close()


def bool_breakpoint(frame, bp_loc, dict):
    """
     bool xpc_dictionary_get_bool(xpc_object_t dictionary, const char *key);
    """

    print("\n-------- xpc_dictionary_get_bool -------\n")
    log("\n-------- xpc_dictionary_get_bool -------\n")

    # Get the general purpose registers
    registers = get_frame().GetRegisters()

    for value in registers:
        if "general purpose" in value.GetName().lower():
            GPRS = value
            break
    print("\n")
    for register in GPRS:
        if register.GetName() == "x0":
            response = lldb.SBCommandReturnObject()
            interpreter = lldb.debugger.GetCommandInterpreter()
            interpreter.HandleCommand("expr -o -- {0}".format(register.GetValue()), response)
            if response.Succeeded():
                output = response.GetOutput()
                if output:
                    print("-------- XPC Dictionary ------------------\n")
                    print(output)
                    log("-------- XPC Dictionary ------------------\n")
                    log("{0}".format(output))
        if register.GetName() == "x1":
            response = lldb.SBCommandReturnObject()
            interpreter = lldb.debugger.GetCommandInterpreter()
            interpreter.HandleCommand("x/s {0}".format(register.GetValue()), response)
            if response.Succeeded():
                output = response.GetOutput()
                if output:
                    print("------- KEY ------------------------------\n")
                    print(output)
                    log("------- KEY ------------------------------\n")
                    log("{0}".format(output))


def string_breakpoint(frame, bp_loc, dict):
    """
    const char * xpc_dictionary_get_string(xpc_object_t dictionary, const char *key);
    """

    print("\n-------- xpc_dictionary_get_string -------\n")
    log("\n-------- xpc_dictionary_get_string -------\n")

    # Get the general purpose registers
    registers = get_frame().GetRegisters()

    for value in registers:
        if "general purpose" in value.GetName().lower():
            GPRS = value
            break
    print("\n")
    for register in GPRS:
        if register.GetName() == "x0":
            response = lldb.SBCommandReturnObject()
            interpreter = lldb.debugger.GetCommandInterpreter()
            interpreter.HandleCommand("expr -o -- {0}".format(register.GetValue()), response)
            if response.Succeeded():
                output = response.GetOutput()
                if output:
                    print("-------- XPC Dictionary ------------------\n")
                    print(output)
                    log("-------- XPC Dictionary ------------------\n")
                    log("{0}".format(output))
        if register.GetName() == "x1":
            response = lldb.SBCommandReturnObject()
            interpreter = lldb.debugger.GetCommandInterpreter()
            interpreter.HandleCommand("x/s {0}".format(register.GetValue()), response)
            if response.Succeeded():
                output = response.GetOutput()
                if output:
                    print("------- KEY ------------------------------\n")
                    print(output)
                    log("------- KEY ------------------------------\n")
                    log("{0}".format(output))


def uint64_breakpoint(frame, bp_loc, dict):
    """
    uint64_t xpc_dictionary_get_uint64(xpc_object_t dictionary, const char *key);
    """

    print("\n-------- xpc_dictionary_get_uint64 -------\n")
    log("\n-------- xpc_dictionary_get_uint64 -------\n")

    # Get the general purpose registers
    registers = get_frame().GetRegisters()

    for value in registers:
        if "general purpose" in value.GetName().lower():
            GPRS = value
            break
    print("\n")
    for register in GPRS:
        if register.GetName() == "x0":
            response = lldb.SBCommandReturnObject()
            interpreter = lldb.debugger.GetCommandInterpreter()
            interpreter.HandleCommand("expr -o -- {0}".format(register.GetValue()), response)
            if response.Succeeded():
                output = response.GetOutput()
                if output:
                    print("-------- XPC Dictionary ------------------\n")
                    print(output)
                    log("-------- XPC Dictionary ------------------\n")
                    log("{0}".format(output))
        if register.GetName() == "x1":
            response = lldb.SBCommandReturnObject()
            interpreter = lldb.debugger.GetCommandInterpreter()
            interpreter.HandleCommand("x/s {0}".format(register.GetValue()), response)
            if response.Succeeded():
                output = response.GetOutput()
                if output:
                    print("------- KEY ------------------------------\n")
                    print(output)
                    log("------- KEY ------------------------------\n")
                    log("{0}".format(output))


def int64_breakpoint(frame, bp_loc, dict):
    """
    int64_t xpc_dictionary_get_int64(xpc_object_t dictionary, const char *key);
    """

    print("\n-------- xpc_dictionary_get_int64 -------\n")
    log("\n-------- xpc_dictionary_get_int64 -------\n")

    # Get the general purpose registers
    registers = get_frame().GetRegisters()

    for value in registers:
        if "general purpose" in value.GetName().lower():
            GPRS = value
            break
    print("\n")
    for register in GPRS:
        if register.GetName() == "x0":
            response = lldb.SBCommandReturnObject()
            interpreter = lldb.debugger.GetCommandInterpreter()
            interpreter.HandleCommand("expr -o -- {0}".format(register.GetValue()), response)
            if response.Succeeded():
                output = response.GetOutput()
                if output:
                    print("-------- XPC Dictionary ------------------\n")
                    print(output)
                    log("-------- XPC Dictionary ------------------\n")
                    log("{0}".format(output))
        if register.GetName() == "x1":
            response = lldb.SBCommandReturnObject()
            interpreter = lldb.debugger.GetCommandInterpreter()
            interpreter.HandleCommand("x/s {0}".format(register.GetValue()), response)
            if response.Succeeded():
                output = response.GetOutput()
                if output:
                    print("------- KEY ------------------------------\n")
                    print(output)
                    log("------- KEY ------------------------------\n")
                    log("{0}".format(output))


def data_breakpoint(frame, bp_loc, dict):
    """
    const void * xpc_dictionary_get_data(xpc_object_t dictionary, const char *key, size_t *length);
    """

    print("\n-------- xpc_dictionary_get_data -------\n")
    log("\n-------- xpc_dictionary_get_data -------\n")

    # Get the general purpose registers
    registers = get_frame().GetRegisters()

    for value in registers:
        if "general purpose" in value.GetName().lower():
            GPRS = value
            break
    print("\n")
    for register in GPRS:
        if register.GetName() == "x0":
            response = lldb.SBCommandReturnObject()
            interpreter = lldb.debugger.GetCommandInterpreter()
            interpreter.HandleCommand("expr -o -- {0}".format(register.GetValue()), response)
            if response.Succeeded():
                output = response.GetOutput()
                if output:
                    print("-------- XPC Dictionary ------------------\n")
                    print(output)
                    log("-------- XPC Dictionary ------------------\n")
                    log("{0}".format(output))
        if register.GetName() == "x1":
            response = lldb.SBCommandReturnObject()
            interpreter = lldb.debugger.GetCommandInterpreter()
            interpreter.HandleCommand("x/s {0}".format(register.GetValue()), response)
            if response.Succeeded():
                output = response.GetOutput()
                if output:
                    print("------- KEY ------------------------------\n")
                    print(output)
                    log("------- KEY ------------------------------\n")
                    log("{0}".format(output))


def xpc(debugger, command, result, internal_dict):
    """
    Setup breakpoints for various XPC functions

    xpc_dictionary_get_int64
    xpc_dictionary_get_bool

    """
    target = debugger.GetSelectedTarget()

    # Create breakpoints
    getint64 = target.BreakpointCreateByName("xpc_dictionary_get_int64")
    getuint64 = target.BreakpointCreateByName("xpc_dictionary_get_uint64")
    getbool = target.BreakpointCreateByName("xpc_dictionary_get_bool")
    getstring = target.BreakpointCreateByName("xpc_dictionary_get_string")
    getdata = target.BreakpointCreateByName("xpc_dictionary_get_data")

    # Set callback functions
    getint64.SetScriptCallbackFunction("xpc.int64_breakpoint")
    getuint64.SetScriptCallbackFunction("xpc.uint64_breakpoint")
    getbool.SetScriptCallbackFunction("xpc.bool_breakpoint")
    getstring.SetScriptCallbackFunction("xpc.string_breakpoint")
    getdata.SetScriptCallbackFunction("xpc.data_breakpoint")


def get_frame():
    """
    Get the current frame and return it to the calling function
    """
    ret = None

    for t in lldb.debugger.GetSelectedTarget().process:
        if t.GetStopReason() != lldb.eStopReasonNone and t.GetStopReason() != lldb.eStopReasonInvalid:
            ret = t.GetFrameAtIndex(0)
    return ret


def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand("platform select remote-ios")
    debugger.HandleCommand("process connect connect://localhost:6666")
    debugger.HandleCommand("command script add -f xpc.xpc xpc")
