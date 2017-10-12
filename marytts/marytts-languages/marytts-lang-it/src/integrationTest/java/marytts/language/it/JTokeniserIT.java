package marytts.language.it;

import java.util.Locale;

import org.junit.Test;

import marytts.language.it.JTokeniser;
import marytts.modules.ModuleRegistry;
import marytts.tests.modules.MaryModuleTestCase;

public class JTokeniserIT extends MaryModuleTestCase {

	public JTokeniserIT() throws Exception {
		super(true);
		module = ModuleRegistry.getModule(JTokeniser.class);
	}

	protected String inputEnding() {
		return "txt";
	}

	protected String outputEnding() {
		return "tokenised";
	}

	@Test
	public void testDots1() throws Exception {
		processAndCompare("dots1", Locale.ITALIAN);
	}

	@Test
	public void testDots2() throws Exception {
		processAndCompare("dots2", Locale.ITALIAN);
	}

	@Test
	public void testDots3() throws Exception {
		processAndCompare("dots3", Locale.ITALIAN);
	}

	@Test
	public void testExclam() throws Exception {
		processAndCompare("exclam", Locale.ITALIAN);
	}

	@Test
	public void testQuest() throws Exception {
		processAndCompare("quest", Locale.ITALIAN);
	}
}
