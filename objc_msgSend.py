try:
    import lldb
    import datetime
except:
    pass

def log(d, id):
    """
    Log results for the objc_msgSend() hook
    """
    if id == "ID":
        with open("{0}-objc_msgSend-log".format(datetime.date.today()), "a+") as f:
            f.writelines("%s" % d.strip("\n"))
            f.close()
    else:
        with open("{0}-objc_msgSend-log".format(datetime.date.today()), "a+") as f:
            f.writelines("%s" % d)
            f.close()

def objc_msgSend(debugger, command, result, internal_dict):
    """
    Setup breakpoint for objc_msgSend() and pass control to
    a callback function
    """
    target = debugger.GetSelectedTarget()
    breakpoint = target.BreakpointCreateByName("objc_msgSend")
    breakpoint.SetScriptCallbackFunction("objc_msgSend.getStructure")

def getStructure(frame, bp_loc, dict):
    """
    Get the structure of the objc_obj that correlates
    to the current objc_msgSend() call
    """
    # Get general purpose registers
    registers = get_frame().GetRegisters()
    for value in registers:
        if "general purpose" in value.GetName().lower():
            GPRS = value
            break
    for reg in GPRS:
        # x0 will hold the ID pointer
        if reg.GetName() == "x0":
            res = lldb.SBCommandReturnObject()
            interpreter = lldb.debugger.GetCommandInterpreter()
            # This evaluates the address in x0 as an object
            interpreter.HandleCommand("expr -o -- {0}".format(reg.GetValue()), res)
            if res.Succeeded():
                output = res.GetOutput()
                if output:
                    print(output)
                    log("".join(["{0} : {1}".format(lldb.debugger.GetSelectedTarget(), datetime.datetime.now()), " : ID : ", output]), "ID")
            # Get the stack-history for the given pointer inside x0
            interpreter.HandleCommand("malloc_info --stack-history {0}".format(reg.GetValue()), res)
            if res.Succeeded():
                output = res.GetOutput()
                if output:
                    print(output)
                    log("".join(["\n{0} : {1}".format(lldb.debugger.GetSelectedTarget(), datetime.datetime.now()), " : malloc : ", output]), "MALLOC")
            # Get the objc_class representation within memory
            interpreter.HandleCommand("memory read --size 8 --format A --count 10 {0}".format(reg.GetValue()), res)
            if res.Succeeded():
                output = res.GetOutput()
                if output:
                    print(output)
                    log("".join(["{0} : {1}".format(lldb.debugger.GetSelectedTarget(), datetime.datetime.now()), " : mem : \n", output]), "MEM")
        # x1 will hold the SEL
        if reg.GetName() == "x1":
            res = lldb.SBCommandReturnObject()
            interpreter = lldb.debugger.GetCommandInterpreter()
            interpreter.HandleCommand("x/s {0}".format(reg.GetValue()), res)
            if res.Succeeded():
                output = res.GetOutput()
                if output:
                    print(output)
                    log("".join(["{0} : {1}".format(lldb.debugger.GetSelectedTarget(), datetime.datetime.now())," : SEL :", output, "\n"]), "SEL")
    # Grap the target process so we can continue after
    # our inspections
    target = lldb.debugger.GetSelectedTarget()
    process = target.GetProcess()
    process.Continue()

def get_frame():
    """
    Get the current frame and return it
    to the calling function
    """
    ret = None
    for t in lldb.debugger.GetSelectedTarget().process:
        if t.GetStopReason() != lldb.eStopReasonNone and t.GetStopReason() != lldb.eStopReasonInvalid:
			ret = t.GetFrameAtIndex(0);
    return ret

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand("platform select remote-ios")
    debugger.HandleCommand("process connect connect://localhost:6666")
    debugger.HandleCommand("command script import lldb.macosx.heap")
    debugger.HandleCommand("command script add -f objc_msgSend.objc_msgSend objc_msgSend")
